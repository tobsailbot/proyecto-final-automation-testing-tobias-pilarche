import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Cargar datos
with open('data/test_data.json') as f:
    data = json.load(f)

def test_agregar_producto_al_carrito(driver):
    # 1. Login (Precondición)
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    
    # 2. Agregar producto
    inventory = InventoryPage(driver)
    assert "Products" in inventory.get_title()
    inventory.add_first_product_to_cart()
    
    # 3. Validar que el contador del carrito es 1
    assert "1" == inventory.get_cart_badge_count()

def test_navegar_al_carrito(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    # Agregar producto al carrito
    inventory = InventoryPage(driver)
    inventory.go_to_cart()
    assert "cart.html" in driver.current_url