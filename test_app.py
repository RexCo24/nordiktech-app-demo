import json
from app import app

def test_api_info():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()
    assert data["name"] == "Inventory API"
    assert data["version"] == "1.0.0"
    assert data["status"] == "running"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "ok"


def test_get_inventory_initial_empty():
    client = app.test_client()
    response = client.get("/inventory")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_add_product():
    client = app.test_client()

    payload = {
        "name": "Apfel",
        "quantity": 10
    }

    response = client.post(
        "/inventory",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201

    data = response.get_json()
    assert data["name"] == "Apfel"
    assert data["quantity"] == 10
    assert "id" in data


def test_inventory_after_adding_product():
    client = app.test_client()
    response = client.get("/inventory")
    assert response.status_code == 200

    data = response.get_json()
    assert len(data) >= 1
    assert data[0]["name"] == "Apfel"
