from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John"

def test_get_user():
    create_response = client.post("/users/", json={"name": "Jane", "email": "jane@example.com"})
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane"
    assert response.json()["email"] == "jane@example.com"

def test_update_user():
    create_response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    user_id = create_response.json()["id"]

    update_response = client.put(f"/users/{user_id}", json={"name": "Alice Updated", "email": "alice.updated@example.com"})
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Alice Updated"
    assert update_response.json()["email"] == "alice.updated@example.com"

def test_delete_user():
    create_response = client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    user_id = create_response.json()["id"]

    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["name"] == "Bob"

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "User not found"