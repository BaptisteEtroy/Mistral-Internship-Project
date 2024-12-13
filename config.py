import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    MISTRAL_API_KEY: str = os.getenv("MISTRAL_API_KEY")
    MISTRAL_API_URL: str = os.getenv(
        "MISTRAL_API_URL", "https://api.mistral.ai/generate"
    )
    DATABASE_DIR: str = os.getenv("DATABASE_DIR", "data")
    MODEL_NAME: str = "mistral-large-latest"
    MAX_TOKENS: int = 256

    def ensure_database_dir(self):
        if not os.path.exists(self.DATABASE_DIR):
            os.makedirs(self.DATABASE_DIR)


settings = Settings()
settings.ensure_database_dir()