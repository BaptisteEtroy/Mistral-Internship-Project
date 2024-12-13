from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

Base = declarative_base()


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role = Column(String, index=True)  # user or chatbot
    content = Column(Text)


def get_engine(db_name: str):
    db_path = f"{settings.DATABASE_DIR}/{db_name}.db"
    return create_engine(
        f"sqlite:///{db_path}", connect_args={"check_same_thread": False}
    )


def get_session(db_name: str):
    engine = get_engine(db_name)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base.metadata.create_all(bind=engine)
    return SessionLocal()
