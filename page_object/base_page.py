from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator: Tuple[str, str], timeout: int = 20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.click()

    def enter_text(self, locator: Tuple[str, str], text: str, timeout: int = 10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        # element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def is_visible(self, locator: Tuple[str, str]) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False