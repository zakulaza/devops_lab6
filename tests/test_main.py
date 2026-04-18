from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Docker and CI/CD!"}

def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert response.json()["status"] == "success"