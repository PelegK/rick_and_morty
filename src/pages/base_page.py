from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.pages.selectors_page import Selectors

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 10
        self.selectors = Selectors

    def get_element(self, selector):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(selector)
        )
        return element

    def click(self, selector):
        WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(selector)).click()

    def set_text(self, selector, text):
        WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(selector)).send_keys(text)

    def clear_text(self, selector):
        WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(selector)).clear()

    def switch_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
    
    def new_tab(self,url):
        self.driver.execute_script("window.open('');")
        self.switch_tab(-1)
        self.driver.get(url)

    def get_elements(self, selector):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_all_elements_located(selector))

    def close_browser(self):
        self.driver.close()