# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from Mistral import app

@pytest.fixture
def client():
    return TestClient(app)
