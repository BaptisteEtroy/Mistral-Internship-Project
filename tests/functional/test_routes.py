# tests/functional/test_routes.py
import pytest


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Mistral le chat" in response.text


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize(
    "question, expected_status",
    [("What is the capital of France?", 200), ("", 422)],
)
def test_query_route(client, question, expected_status):
    response = client.post("/query", json={"question": question})
    assert response.status_code == expected_status
    if expected_status == 200:
        assert "answer" in response.json()
