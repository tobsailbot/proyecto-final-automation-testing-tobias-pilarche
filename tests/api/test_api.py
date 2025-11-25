import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert len(json_data["data"]) > 0

def test_create_user():
    payload = {"name": "Morpheus", "job": "Leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "Morpheus"
    assert "id" in json_data

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204