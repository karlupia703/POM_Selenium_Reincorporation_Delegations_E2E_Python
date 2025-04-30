import time
import pytest
from selenium.common import NoSuchElementException
from faker import Faker
from webdriver_manager.core import driver

from page_object.create_user_page import CreateUserPages
from page_functions.driver_manager import DriverManager
from page_object.create_user_page import CreateUserPages

from config.config import Config
from test_data.translations import Translations

class CreateUserTest:
    def __init__(self):
        self.driver = driver
        self.driver = DriverManager.get_driver()
        self.faker = Faker()
        self.language = Config.language

    def generate_random_email(self, first_name, last_name):
        return f"{first_name.lower()}.{last_name.lower()}@example.com"

    def create_user(self):
        # Test case for creating a new user.
        user_page = CreateUserPages(self.driver)
        expected_texts = Translations.get_translation(Config.language)
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.generate_random_email(first_name, last_name)

        print(f"Creating user: {first_name} {last_name} - {email}")
        user_page.click_on_create_button()
        time.sleep(1)
        user_page.click_on_inside_create_button()
        time.sleep(1)

        assert user_page.is_first_name_error_text(expected_texts["firstNameMinError"]), "First name error mismatch"
        assert user_page.is_last_name_error_text(expected_texts["lastNameMinError"]), "Last name error mismatch"
        assert user_page.is_email_error_text(expected_texts["emailRequiredError"]), "Email error mismatch"
        assert user_page.is_headquarter_error_text(expected_texts["headquarterError"]), "Headquarter error mismatch"

        user_page.enter_first_name(first_name)
        time.sleep(2)
        user_page.enter_last_name(last_name)
        time.sleep(2)
        user_page.enter_email(email)
        time.sleep(2)
        user_page.select_headquarter()
        time.sleep(2)
        user_page.click_on_submit_btn()
        time.sleep(2)
        success_message = user_page.get_success_message()
        print(f"Snackbar Text: {success_message}")


    def test_edit_user(self):
        # Test case for editing an existing user.
        user_page = CreateUserPages(self.driver)
        expected_texts = Translations.get_translation(Config.language)
        updated_last_name = self.faker.last_name()
        first_row = user_page.find_first_row1()
        if not first_row:
            print("ERROR: No row found!")
            return
        time.sleep(2)
        try:
            user_page.click_on_last_name_field(updated_last_name)
        except Exception as e:
            print(f"ERROR: Could not click last name field: {e}")
            return
        user_page.click_on_edit_button()

        # Validate confirmation messages
        assert user_page.is_check_edit_cancel_alert_title(expected_texts["EditTitle"]), "Edit title mismatch"
        assert user_page.is_check_edit_cancel_alert_content(expected_texts["body"]), "Edit body mismatch"

        user_page.click_on_confirm_dialog_box()
        time.sleep(2)
        success_message = user_page.get_snackbar_success_message()
        print(f"Snackbar Text: {success_message}")


    def test_view_user(self):
        user_page = CreateUserPages(self.driver)
        user_page.click_on_view_icon1()
        time.sleep(3)
        user_page.click_on_view_cross_icon()
        time.sleep(2)


    def test_delete_user(self):
        driver = DriverManager.get_driver()
        expected_texts = Translations.get_translation(Config.language)
        user_page = CreateUserPages(driver)
        user_page.clear_previous_notifications()
        user_page.click_delete_button()
        assert user_page.is_check_delete_alert_title(expected_texts["deleteAlertTitle"]), "Title mismatch."
        assert user_page.is_check_delete_alert_content(expected_texts["deleteBody"]), "Body mismatch."
        user_page.confirm_deletion()
        success_message = user_page.get_notification_message2()
        print(f"Snackbar Text: {success_message}")


    def test_search_user(self):
        user_page = CreateUserPages(self.driver)
        try:
            first_row = user_page.get_first_row()
            uuid = user_page.extract_uuid_from_row(first_row)
            user_name = user_page.get_user_name(first_row, uuid)
            print(f"Extracted userName: {user_name}")
            user_page.search_for_user_name(user_name)
            time.sleep(1)
            user_page.clear_search()
            time.sleep(1)
            user_page.search_with_random_text_and_check_no_results()
            time.sleep(1)
        except NoSuchElementException as e:
            print(f"Error: {e}")


    def test_filter_functionality(self):
        user_page = CreateUserPages(self.driver)
        user_page.open_filter_dropdown()
        time.sleep(3)
        user_page.select_option_ao()
        time.sleep(1)
        user_page.select_option_cl()
        time.sleep(1)
        user_page.close_filter_dropdown()
        time.sleep(1)
        user_page.click_on_clear_filters()
        time.sleep(1)
        user_page.open_status_filter_dropdown()
        time.sleep(1)
        user_page.click_on_clear_filters()
        time.sleep(1)


    def test_pagination(self):
        user_page = CreateUserPages(self.driver)
        if user_page.is_right_arrow_available():
            if user_page.is_right_arrow_enabled():
                print("Right pagination arrow is enabled.")
                user_page.click_right_arrow()
                time.sleep(2)
            else:
                print("Right pagination arrow is disabled.")
        else:
            print("Right pagination arrow is not available.")

        if user_page.is_left_arrow_available():
            if user_page.is_left_arrow_enabled():
                print("Left pagination arrow is enabled.")
                user_page.click_left_arrow()
                time.sleep(2)
            else:
                print("Left pagination arrow is disabled.")
        else:
            print("Left pagination arrow is not available.")


    def test_already_exist_user(self):
        user_page = CreateUserPages(self.driver)
        faker = Faker()
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()

        user_page.click_create_button()
        user_page.fill_user_details(first_name, last_name, email)
        user_page.select_headquarter1()
        user_page.click_submit_button()
        success_message = user_page.get_success_message()
        print(f"Snackbar Text: {success_message}")

        # Attempt to create duplicate user
        user_page.click_create_button()
        user_page.fill_user_details(first_name, last_name, email)
        user_page.select_headquarter()
        user_page.toggle_status()
        user_page.click_submit_button()
        success_message = user_page.get_email_already_exist_message()
        print(f"Snackbar Text: {success_message}")

        user_page.click_cancel_button()
        user_page.click_yes_button()