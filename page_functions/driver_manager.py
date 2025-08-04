import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverManager:
    _driver = None
    keep_browser_open = True

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # Check if we should use a remote Selenium server
            remote_url = os.environ.get('SELENIUM_REMOTE_URL')

            # Check if we should run in headless mode
            headless = os.environ.get('SELENIUM_HEADLESS', '0') == '1'

            if remote_url:
                print(f"Using remote Selenium server at {remote_url}")
                options = Options()
                if headless:
                    options.add_argument('--headless')
                    print("Running in headless mode")

                cls._driver = webdriver.Remote(
                    command_executor=remote_url,
                    options=options
                )
            else:
                print("Using local Chrome driver")
                options = Options()
                if headless:
                    options.add_argument('--headless')
                    print("Running in headless mode")

                service = Service(ChromeDriverManager().install())
                cls._driver = webdriver.Chrome(service=service, options=options)

            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if not cls.keep_browser_open and cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
