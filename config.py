import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    MISTRAL_API_KEY: str = os.getenv("MISTRAL_API_KEY")
    MISTRAL_API_URL: str = os.getenv("MISTRAL_API_URL", "https://api.mistral.ai/generate")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data/app.db")
    MODEL_NAME: str = "mistral-large-latest"
    MAX_TOKENS: int = 256

settings = Settings()