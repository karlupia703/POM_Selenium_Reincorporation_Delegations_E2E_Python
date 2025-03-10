from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selectors
    language_dropdown = (By.CSS_SELECTOR, "[data-test-id='login-language-select']")
    google_sign_in_button = (By.CSS_SELECTOR, "[data-test-id='login-button-text']")
    email_input = (By.XPATH, "//input[@type='email']")
    email_next_button= (By.XPATH, "//span[text()='Next']")
    password_input = (By.XPATH, "//input[@type='password']")
    password_next_button= (By.XPATH, "//span[text()='Next']")

    # Assertions Selectors
    login_title= (By.CSS_SELECTOR, "[data-test-id='login-app-title']")
    access_with_google_text = (By.CSS_SELECTOR, "[data-test-id='login-app-title-sub-text']")

    def click_language_dropdown(self):
        self.driver.find_element(*self.language_dropdown).click()

    def select_language(self, language_code: str):
        language_option = (By.CSS_SELECTOR, f"[data-value='{language_code}']")
        self.driver.find_element(*language_option).click()

    def get_selected_language(self) -> str:
        try:
            language_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.language_dropdown)
            )
            return language_element.text.strip()
        except:
            print("Language dropdown not found")
            return None  # Or handle the error accordingly

    def click_google_sign_in(self):
        self.driver.find_element(*self.google_sign_in_button).click()

    def enter_email(self, email: str):
        email_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.email_input)
        )
        email_input.send_keys(email)

    def click_email_next(self):
        self.driver.find_element(*self.email_next_button).click()

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        )
        password_input.send_keys(password)

    def click_password_next(self):
        self.driver.find_element(*self.password_next_button).click()

    def get_element_text(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text.strip()

    def is_title_correct(self, expected_title: str) -> bool:
        return self.get_element_text(self.login_title) == expected_title

    def is_google_button_correct(self, expected_text: str) -> bool:
        return self.get_element_text(self.google_sign_in_button) == expected_text

    def is_access_with_google_text_correct(self, expected_text: str) -> bool:
        return self.get_element_text(self.access_with_google_text) == expected_text
