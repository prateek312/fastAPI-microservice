# tests/test_order_service.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    order_data = {
        "user_id": "7c11e1ce2741",
        "product_code": "classic-box"
    }
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    assert "order_id" in response.json()

