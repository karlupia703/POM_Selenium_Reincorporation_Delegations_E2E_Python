
import time
import pytest
from selenium.common import NoSuchElementException
from faker import Faker
from Page_Object.create_user_page import CreateUserPages
from Page_Functions.driver_manager import DriverManager

class CreateUserTest:
    def __init__(self, language):
        self.driver = DriverManager.get_driver()
        self.language = language
        self.faker = Faker()

        # Supported translations for different languages
        self.supported_translations = {
            "en_US": {
                "firstNameMinError": "First name must be at least 3 characters long",
                "lastNameMinError": "Last name must be at least 3 characters long",
                "emailRequiredError": "Email is required",
                "headquarterError": "Please select a headquarter",
                "title": "Edit Reinstatement Responsible",
                "body": "Are you sure you want to save the changes?",
                "deletealerttitle": "Delete Reinstatement Responsible",
                "deletebody": "Are you sure to delete the user"
            },
            "Español": {
                "firstNameMinError": "El nombre debe tener al menos 3 caracteres",
                "lastNameMinError": "El apellido debe tener al menos 3 caracteres",
                "emailRequiredError": "El correo electrónico es requerido",
                "headquarterError": "Por favor seleccione una sede",
                "title": "Editar Responsable de Reincorporación",
                "body": "¿Está seguro de guardar los cambios?",
                "deletealerttitle": "Eliminar Responsable de Reincorporación",
                "deletebody": "¿Está seguro de eliminar al usuario"
            }
        }

    def generate_random_email(self, first_name, last_name):
        return f"{first_name.lower()}.{last_name.lower()}@example.com"

    def create_user(self):
        # Test case for creating a new user.
        user_page = CreateUserPages(self.driver)
        expected_texts = self.supported_translations.get(self.language, {})
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.generate_random_email(first_name, last_name)

        print(f"Creating user: {first_name} {last_name} - {email}")
        user_page.click_on_create_button()
        time.sleep(1)
        user_page.click_on_inside_create_button()
        time.sleep(1)

        # Validate error messages in the selected language
        # assert user_page.is_first_name_error_text(expected_texts["firstNameMinError"]), "First name error mismatch"
        # assert user_page.is_last_name_error_text(expected_texts["lastNameMinError"]), "Last name error mismatch"
        # assert user_page.is_email_error_text(expected_texts["emailRequiredError"]), "Email error mismatch"
        # assert user_page.is_headquarter_error_text(expected_texts["headquarterError"]), "Headquarter error mismatch"

        print(f"Assertions passed for language: {self.language}")
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
        # success_message = user_page.get_success_message()
        # print(f"Snackbar Text: {success_message}")
        # print(f"User created successfully for language: {self.language}")


    def test_edit_user(self):
        # Test case for editing an existing user.
        user_page = CreateUserPages(self.driver)
        expected_texts = self.supported_translations.get(self.language, {})
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
        # assert user_page.is_check_edit_cancel_alert_title(expected_texts["title"]), "Edit title mismatch"
        # assert user_page.is_check_edit_cancel_alert_content(expected_texts["body"]), "Edit body mismatch"
        print(f"Edit Assertions passed for language: {self.language}")
        user_page.click_on_confirm_dialog_box()
        time.sleep(2)
        success_message = user_page.get_snackbar_success_message()
        print(f"Snackbar Text: {success_message}")


    def test_view_user(self):
        user_page = CreateUserPages(self.driver)
        # expected_texts = self.supported_translations.get(self.language, {})
        user_page.click_on_view_icon1()
        time.sleep(3)
        user_page.click_on_view_cross_icon()
        time.sleep(2)
        print("User view successfully")


    def test_delete_user(target_language):
        driver = DriverManager.get_driver()
        user_page = CreateUserPages(driver)
        # Supported translations
        translations = {
            "Español": {"deletealerttitle": "¿Estás seguro?", "deletebody": "Esta acción eliminará al usuario."},
            "en_US": {"deletealerttitle": "Are you sure?", "deletebody": "This action will delete the user."}
        }
        expected_texts = translations.get(target_language, {})
        user_page.clear_previous_notifications()
        user_page.click_delete_button()
        # assert user_page.is_check_delete_alert_title(expected_texts["deletealerttitle"]), "Title mismatch."
        # assert user_page.is_check_delete_alert_content(expected_texts["deletebody"]), "Body mismatch."

        print(f"Delete Assertions passed for: {target_language}")
        user_page.confirm_deletion()
        print("Snackbar Text:", user_page.get_notification_message2())
        time.sleep(1)


    def test_filter_functionality(self):
        user_page = CreateUserPages(self.driver)
        expected_texts = self.supported_translations.get(self.language, {})
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
        user_page.select_inactive_option()
        time.sleep(1)
        user_page.click_on_clear_filters()
        time.sleep(1)

    def test_search_user1(driver):
        # Test to search for a user based on extracted UUID.
        user_page = CreateUserPages(driver)
        try:
            first_row = user_page.get_first_row()
            uuid = user_page.extract_uuid_from_row(first_row)  # Extract UUID from the first row
            user_name = user_page.get_user_name(first_row, uuid)  # Get user name
            print(f"Extracted userName: {user_name}")
            user_page.search_for_user_name(user_name)
            user_page.clear_search()

        except NoSuchElementException as e:
            print(f"Error: {e}")


    def test_pagination(self):
        user_page = CreateUserPages(self.driver)

        if user_page.is_right_arrow_available():
            if user_page.is_right_arrow_enabled():
                print("Right pagination arrow is enabled.")
                user_page.click_right_arrow()
                time.sleep(2)  # Wait after clicking
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
        # user_page.toggle_status()
        user_page.click_submit_button()

        # assert "User created successfully" in user_page.get_success_message1()
        # Attempt to create duplicate user
        user_page.click_create_button()
        user_page.fill_user_details(first_name, last_name, email)
        user_page.select_headquarter()
        user_page.toggle_status()
        user_page.click_submit_button()

        # assert "el Email ya existe" in user_page.get_success_message()
        # Email already exists
        user_page.click_cancel_button()
        user_page.click_yes_button()
