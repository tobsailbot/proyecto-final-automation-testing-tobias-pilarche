from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Selectores
    PRODUCT_TITLE = (By.CLASS_NAME, "title")
    FIRST_ADD_TO_CART_BTN = (By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def add_first_product_to_cart(self):
        self.click(self.FIRST_ADD_TO_CART_BTN)

    def get_cart_badge_count(self):
        # Devuelve el número pequeño rojo en el carrito
        return self.get_text(self.CART_BADGE)
        
    def go_to_cart(self):
        self.click(self.CART_ICON)