import json
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_classify_messages():
    with open("../../data/conversations.json", encoding="utf-8") as f:
        data = json.load(f)
    messages = data["conversations"]

    erros = 0

    for msg in messages:
        payload = {
            "message": msg["message"]
        }

        response = client.post("/classify", json=payload)

        if response.status_code != 200:
            erros += 1
        ##assert response.status_code == 200

        data = response.json()

        assert "category" in data
        assert "confidence" in data

        assert isinstance(data["category"], str)
        assert isinstance(data["confidence"], float)
        assert 0.0 <= data["confidence"] <= 1.0
