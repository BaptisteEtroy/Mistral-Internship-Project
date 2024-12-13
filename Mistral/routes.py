from fastapi import APIRouter, HTTPException
from Mistral.models import Message, get_session
from Mistral.pydantic_models import QueryRequest, QueryResponse
from mistralai import Mistral
from config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

client = Mistral(api_key=settings.MISTRAL_API_KEY)


@router.post("/query", response_model=QueryResponse)
def query_documents(request: QueryRequest):
    try:
        db = get_session(request.db_name)
        conversation_history = db.query(Message).all()

        # Ensure the conversation history ends with a user message
        if not conversation_history or conversation_history[-1].role != "user":
            new_message = Message(role="user", content=request.question)
            db.add(new_message)
            db.commit()
            conversation_history.append(new_message)

        chat_response = client.chat.complete(
            model=settings.MODEL_NAME,
            messages=[
                {"role": msg.role, "content": msg.content}
                for msg in conversation_history
            ],
            max_tokens=settings.MAX_TOKENS,
        )

        if not chat_response.choices:
            answer = "I’m sorry, I don’t have an answer."
        else:
            answer = chat_response.choices[0].message.content

        assistant_message = Message(role="assistant", content=answer)
        db.add(assistant_message)
        db.commit()

        return QueryResponse(question=request.question, answer=answer)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
