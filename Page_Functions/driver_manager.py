from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverManager:
    _driver = None
    keep_browser_open = True  # ✅ Set to `True` to keep the browser open

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            service = Service(ChromeDriverManager().install())
            cls._driver = webdriver.Chrome(service=service)
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if not cls.keep_browser_open and cls._driver is not None:
            cls._driver.quit()
            cls._driver = None