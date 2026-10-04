from fastapi.testclient import TestClient
from features.main import app

client = TestClient(app)


def test_summary():
    payload = client.post("/analyze", json={"rows": [{'split': 'train', 'feature': 10}, {'split': 'train', 'feature': 30}, {'split': 'test', 'feature': 20}]}).json()
    assert payload["mean"] == 20.0
    assert payload["by_split"]["train"]


def test_empty_is_refused():
    assert client.post("/analyze", json={"rows": []}).status_code == 422
