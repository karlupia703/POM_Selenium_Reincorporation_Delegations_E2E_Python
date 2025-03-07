from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from Page_Functions.driver_manager import DriverManager
# from Page_Functions import DriverManager



class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # self.url = DriverManager.get_url("login")  # Centralized URL
        self.wait = WebDriverWait(driver, 10)

    # Selectors
    LANGUAGE_DROPDOWN = (By.CSS_SELECTOR, "[data-test-id='login-language-select']")
    GOOGLE_SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[data-test-id='login-button-text']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    EMAIL_NEXT_BUTTON = (By.XPATH, "//span[text()='Next']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PASSWORD_NEXT_BUTTON = (By.XPATH, "//span[text()='Next']")

    # Assertions Selectors
    LOGIN_TITLE = (By.CSS_SELECTOR, "[data-test-id='login-app-title']")
    ACCESS_WITH_GOOGLE_TEXT = (By.CSS_SELECTOR, "[data-test-id='login-app-title-sub-text']")

    def click_language_dropdown(self):
        self.driver.find_element(*self.LANGUAGE_DROPDOWN).click()

    def select_language(self, language_code: str):
        language_option = (By.CSS_SELECTOR, f"[data-value='{language_code}']")
        self.driver.find_element(*language_option).click()

    def get_selected_language(self) -> str:
        try:
            language_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LANGUAGE_DROPDOWN)
            )
            return language_element.text.strip()
        except:
            print("Language dropdown not found")
            return None  # Or handle the error accordingly


    # correct
    # def get_selected_language(self) -> str:
    #     language_element = self.driver.find_element(*self.LANGUAGE_DROPDOWN)
    #     return language_element.text.strip()

    def click_google_sign_in(self):
        self.driver.find_element(*self.GOOGLE_SIGN_IN_BUTTON).click()

    # def enter_email(self, email: str):
    #     self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_email(self, email: str):
        email_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.EMAIL_INPUT)
        )
        email_input.send_keys(email)

    def click_email_next(self):
        self.driver.find_element(*self.EMAIL_NEXT_BUTTON).click()

    # def enter_password(self, password: str):
    #     self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        password_input.send_keys(password)

    def click_password_next(self):
        self.driver.find_element(*self.PASSWORD_NEXT_BUTTON).click()



    def get_element_text(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text.strip()

    def is_title_correct(self, expected_title: str) -> bool:
        return self.get_element_text(self.LOGIN_TITLE) == expected_title

    def is_google_button_correct(self, expected_text: str) -> bool:
        return self.get_element_text(self.GOOGLE_SIGN_IN_BUTTON) == expected_text

    def is_access_with_google_text_correct(self, expected_text: str) -> bool:
        return self.get_element_text(self.ACCESS_WITH_GOOGLE_TEXT) == expected_text
