import pytest
import json
from pages.login_page import LoginPage

# Cargar datos
with open('data/test_data.json') as f:
    data = json.load(f)

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(data['valid_user'], data['password'])
    assert "inventory.html" in driver.current_url

@pytest.mark.parametrize("usuario, password, mensaje_esperado", [
    ("locked_out_user", "secret_sauce", "Epic sadface"),
    ("usuario_inexistente", "secret_sauce", "Username and password do not match"),
    ("", "secret_sauce", "Username is required")
])
def test_login_casos_negativos(driver, usuario, password, mensaje_esperado):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(usuario, password)
    assert mensaje_esperado in login_page.get_error_message()

def test_login_fallido_usuario_bloqueado(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(data['locked_user'], data['password'])
    assert "Epic sadface" in login_page.get_error_message()