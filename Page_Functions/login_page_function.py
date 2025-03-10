import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Page_Functions.driver_manager import DriverManager
from Page_Object.login_page import LoginPage

class TestLogin:
    def __init__(self, base_url):
        self.base_url = base_url

    def setup_method(self):
        # Initialize WebDriver and navigate to the login page.
        self.driver = DriverManager.get_driver()
        self.driver.get(self.base_url)
        self.page = LoginPage(self.driver)
        self.translations = {
            "en_US": {
                "title": "Reincorporation Delegations",
                "button": "Sign in with Google",
                "accessWithGoogle": "Access to reincorporation delegations"
            },
            "Español": {
                "title": "Responsables de Reincorporación",
                "button": "Accede con Google",
                "accessWithGoogle": "Acceso a delegaciones de reincorporación"
            }
        }

    @pytest.mark.parametrize("target_language", ["Español"])
    def test_login_user(self, target_language):
        # Perform login with the specified language.
        expected_texts = self.translations.get(target_language, {})
        self.switch_language_if_needed(target_language, expected_texts)
        self.page.click_google_sign_in()
        self.handle_google_login()

    def switch_language_if_needed(self, target_language, expected_texts):
        # Switch the language if it's different from the target.
        current_language = self.page.get_selected_language().strip().split("(")[0].strip()

        if current_language.lower() != target_language.lower():
            self.page.click_language_dropdown()
            time.sleep(2)
            self.page.select_language(target_language)
            time.sleep(2)
        self.verify_login_texts(expected_texts)

    def verify_login_texts(self, expected_texts):
        # Verify that login page texts match the expected values.
        assert self.page.is_title_correct(expected_texts["title"]), "Title text mismatch"
        assert self.page.is_google_button_correct(expected_texts["button"]), "Google button text mismatch"
        assert self.page.is_access_with_google_text_correct(expected_texts["accessWithGoogle"]), "Access with Google text mismatch"

    def handle_google_login(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) > 1)

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        time.sleep(3)
        self.page.enter_email("rajni.1156@zenmonk.tech")
        self.page.click_email_next()
        time.sleep(3)
        self.page.enter_password("Rajnikar2022")
        self.page.click_password_next()
        time.sleep(3)

        self.driver.switch_to.window(original_window)
        time.sleep(3)





