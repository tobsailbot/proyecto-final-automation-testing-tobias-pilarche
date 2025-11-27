import requests
import pytest

# URL Base de JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    """
    Caso 1: Obtener lista de usuarios (GET)
    Valida que devuelve status 200 y una lista no vacía.
    """
    endpoint = f"{BASE_URL}/users"
    response = requests.get(endpoint)
    
    # 1. Validar Status Code
    assert response.status_code == 200, f"Falló GET. Status: {response.status_code}"
    
    # 2. Validar estructura de respuesta
    json_data = response.json()
    
    # JSONPlaceholder devuelve una lista directa de usuarios (List[dict])
    assert isinstance(json_data, list), "La respuesta debería ser una lista"
    assert len(json_data) > 0, "La lista de usuarios no debería estar vacía"
    
    # 3. Validar datos de un usuario (ejemplo: que tenga email)
    first_user = json_data[0]
    assert "email" in first_user
    assert "id" in first_user

def test_create_post():
    """
    Caso 2: Crear un recurso (POST)
    Valida que devuelve status 201 y retorna el objeto con ID.
    """
    endpoint = f"{BASE_URL}/posts"
    payload = {
        "title": "Proyecto Final QA",
        "body": "Automatización con Python y Selenium",
        "userId": 1
    }
    
    response = requests.post(endpoint, json=payload)
    
    # 1. Validar Status Code (201 Created)
    assert response.status_code == 201, f"Falló POST. Status: {response.status_code}"
    
    # 2. Validar contenido
    json_data = response.json()
    assert json_data["title"] == "Proyecto Final QA"
    assert "id" in json_data

def test_delete_post():
    """
    Caso 3: Eliminar un recurso (DELETE)
    Valida que devuelve status 200.
    """
    # borrar el post número 1
    endpoint = f"{BASE_URL}/posts/1"
    
    response = requests.delete(endpoint)
    
    # JSONPlaceholder devuelve 200 OK en Delete
    assert response.status_code == 200, f"Falló DELETE. Status: {response.status_code}"