import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
    # ----------------------------------------

    def click(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
            self.logger.info(f"Click realizado en elemento: {locator}")
        except Exception as e:
            self.logger.error(f"Error al hacer click en {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Texto escrito en {locator}")
        except Exception as e:
            self.logger.error(f"Error al escribir en {locator}: {e}")
            raise

    def get_text(self, locator):
        try:
            element = self.find_element(locator)
            text = element.text
            self.logger.info(f"Texto obtenido de {locator}: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Error al obtener texto de {locator}: {e}")
            raise