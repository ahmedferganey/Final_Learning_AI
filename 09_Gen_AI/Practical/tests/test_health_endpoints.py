from fastapi.testclient import TestClient

from services.chat_service.app.main import app as chat_app
from services.rag_service.app.main import app as rag_app
from services.agent_service.app.main import app as agent_app
from services.eval_service.app.main import app as eval_app


def test_chat_health() -> None:
    client = TestClient(chat_app)
    response = client.get("/health")
    assert response.status_code == 200


def test_rag_health() -> None:
    client = TestClient(rag_app)
    response = client.get("/health")
    assert response.status_code == 200


def test_agent_health() -> None:
    client = TestClient(agent_app)
    response = client.get("/health")
    assert response.status_code == 200


def test_eval_health() -> None:
    client = TestClient(eval_app)
    response = client.get("/health")
    assert response.status_code == 200
