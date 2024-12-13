# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from Mistral import app
from Mistral.models import get_session, Base


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def setup_test_db():
    # Creating a test database session for pytests
    db = get_session("test")
    Base.metadata.create_all(bind=db.bind)  # Ensure tables are created
    yield db
    # Cleanup code: droping all tables after tests are done
    Base.metadata.drop_all(bind=db.bind)
