from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from config import settings
from mistralai import Mistral
from Mistral.models import Base, Message 
from Mistral.pydantic_models import QueryRequest, QueryResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base.metadata.create_all(bind=engine)

client = Mistral(api_key=settings.MISTRAL_API_KEY)

def get_conversation_messages():
    db = SessionLocal()
    try:
        msgs = db.query(Message).all()
        return [{"role": msg.role, "content": msg.content} for msg in msgs]
    finally:
        db.close()

def add_message(role: str, content: str):
    db = SessionLocal()
    try:
        m = Message(role=role, content=content)
        db.add(m)
        db.commit()
        db.refresh(m)
        return m
    finally:
        db.close()

# Add this new model
class QueryRequest(BaseModel):
    question: constr(min_length=1, strip_whitespace=True)

@router.post("/query", response_model=QueryResponse)
def query_documents(request: QueryRequest):
    # Fetch conversation history from DB
    conversation_history = get_conversation_messages()

    # Add the user message
    add_message("user", request.question)

    # Refresh conversation history
    conversation_history = get_conversation_messages()

    # Call Mistral
    try:
        chat_response = client.chat.complete(
            model=settings.MODEL_NAME,
            messages=conversation_history,
            max_tokens=settings.MAX_TOKENS
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if not chat_response.choices:
        answer = "I’m sorry, I don’t have an answer."
    else:
        answer = chat_response.choices[0].message.content

    # Store assistant’s response
    add_message("assistant", answer)

    return QueryResponse(question=request.question, answer=answer)