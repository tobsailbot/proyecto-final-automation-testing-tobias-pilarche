import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import datetime

@pytest.fixture(scope="function")
def driver(request):
    # Setup
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--reduce-security-for-testing")
    chrome_options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    
    yield driver # Aquí se ejecuta el test
    
    # Teardown (Cerrar navegador)
    driver.quit()

# Hook para capturar pantalla si falla el test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver') # Recuperamos el driver del test
        if driver:
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"reports/screenshot_{item.name}_{now}.png"
            driver.save_screenshot(screenshot_name)
            print(f" Screenshot guardado: {screenshot_name}")