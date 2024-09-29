import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope='session')
def browser():
    service = Service(ChromeDriverManager().install())    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://www.google.com/?hl=en")
    driver.maximize_window()

    yield driver

    time.sleep(1)
    driver.quit()

