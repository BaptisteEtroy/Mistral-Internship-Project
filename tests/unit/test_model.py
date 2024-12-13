# tests/unit/test_model.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Mistral.models import Base, Message

# Setup an in-memory SQLite database for testing
engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(bind=engine)

def setup_module(module):
    # Create tables in the test database
    Base.metadata.create_all(bind=engine)

def test_create_message():
    # Create a new session
    session = SessionLocal()
    try:
        # Add a new message
        new_message = Message(role="user", content="Hello, world!")
        session.add(new_message)
        session.commit()

        # Query the message
        queried_message = session.query(Message).filter_by(role="user").first()
        assert queried_message is not None
        assert queried_message.content == "Hello, world!"
    finally:
        session.close()
