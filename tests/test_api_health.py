from fastapi.testclient import TestClient
from api.main import app

def test_api_home():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
