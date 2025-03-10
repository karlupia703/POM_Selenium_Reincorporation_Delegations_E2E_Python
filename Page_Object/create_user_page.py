import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import pytest

class CreateUserPages:  # Class names should be in PascalCase

    def __init__(self, driver):
        """
        Initializes the CreateUserPage object.

        Args:
            driver: The Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Initialize WebDriverWait

        # Using explicit waits for element location for create user
        self.create_btn = (By.CSS_SELECTOR, "[data-test-id=\"button-responsibleform-create\"]")
        self.inside_btn = (By.CSS_SELECTOR, "[data-test-id=\"custombtn-modal-responsibleform-create-submit\"]")

        # self.first_name_error = (By.CSS_SELECTOR, "[data-test-id=\"customtextfield-input-responsiblename-responsibleform-create\"]")
        # self.first_name_error = (By.XPATH, "/html/body/div[4]/div[3]/div[2]/div/form/div[1]/p")
        # self.last_name_error = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/p")
        # self.email_error = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[3]/p")
        # self.headquarter_error = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[4]/div/p")

        self.firstname = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[1]/div/input")
        self.lastname = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input")
        self.emailaddress = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[3]/div/input")
        self.headquarter = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[4]/div/div/div/button")
        self.dropdown_options = (By.XPATH, "//ul[@role='listbox']/li")
        self.submit = (By.CSS_SELECTOR, "[data-test-id=\"custombtn-modal-responsibleform-create-submit\"]")
        self.success_message_of_createUser = (By.CSS_SELECTOR, "#notistack-snackbar .MuiBox-root")

        # Using element location for edit user
        self.find_first_row = (By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(5) div:nth-child(1) button:nth-child(2) svg")
        self.last_name_field = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input")
        self.clear_last_name = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input")
        self.edit_button = (By.XPATH, "/html/body/div[5]/div[3]/div[3]/button[2]")
        self.confirm_dialog_box = (By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/button[2]")
        self.edit_cancel_alert_title = (By.CSS_SELECTOR, "[data-test-id=\"dialogBox-title-alertBox-responsiblitiesform-edit\"]")
        self.edit_cancel_alert_content = (By.CSS_SELECTOR, "[data-test-id=\"dialogBox-content-alertBox-responsiblitiesform-edit\"]")
        self.edit_snackbar_message = (By.XPATH, "(//div[@class='notistack-Snackbar go3963613292'])[1]")

        # Using element location for view user
        self.find_first_row_view_icon = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/table/tbody/tr[1]/td[5]/div/button[1]")
        self.cross_icon_view = (By.CSS_SELECTOR, "[data-test-id=\"customdialog-canclebtn-view-viewresponsible-reinstatement-responsibles-table-list-page-reinstatement\"]")

        # Using element location for delete user
        self.delete_button = (By.CSS_SELECTOR, "[data-test-id*='-deleteicon-desktoptable-']")
        self.confirm_delete_button = (By.CSS_SELECTOR, "[data-test-id='custombtn-dialogBox-submit-alertbox-delete-reinstatement-responsibles-table-list-page-reinstatement']")
        self.notification_message = (By.CSS_SELECTOR, "#notistack-snackbar .MuiBox-root")
        self.delete_alert_title = (By.CSS_SELECTOR, "[data-test-id=\"dialogBox-title-alertbox-delete-reinstatement-responsibles-table-list-page-reinstatement\"]")
        self.delete_alert_content = (By.CSS_SELECTOR, "[data-test-id=\"alertbox-deletetext-reinstatement-responsibles-table-list-page-reinstatement\"]")
        self.delete_username = (By.CSS_SELECTOR, "[data-test-id=\"alertbox-deleteusername-reinstatement-responsibles-table-list-page-reinstatement\"]")
        self.notification2 = (By.CSS_SELECTOR, "#notistack-snackbar > .MuiBox-root")

        # Using element location for test filter
        self.filter_dropdown = (By.CSS_SELECTOR, "[data-test-id='chip-label-autocompletefilter-destop-filter-headquarter-page-reinstatement']")
        self.option_ao = (By.CSS_SELECTOR, "[data-test-id='list-item-AO-autocompletefilter-destop-filter-headquarter-page-reinstatement']")
        self.option_cl = (By.CSS_SELECTOR, "[data-test-id='list-item-CL-autocompletefilter-destop-filter-headquarter-page-reinstatement']")
        self.close_dropdown = (By.TAG_NAME, "body")
        self.clear_filters = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[4]")
        self.status_filter_dropdown = (By.CSS_SELECTOR, "[data-test-id='filterchip-arrowdown-icon-filter-status-page-reinstatement']")
        self.inactive_option = (By.CSS_SELECTOR, "[data-test-id=\"filterchip-menu-item-false-filter-status-page-reinstatement\"]")

        # Using element location for search user
        self.wait = WebDriverWait(driver, 10)
        self.table_body = (By.CSS_SELECTOR, "data-test-id='[tablebodyrow-desktoptable-reinstatement-responsibles-table-list-page-reinstatement']")
        self.search_input = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/input")
        self.clear_search_icon = (By.CSS_SELECTOR, "[data-test-id='icon-clear-searchbar-page-reinstatement']")

        # Locators for pagination
        self.right_arrow = (By.CSS_SELECTOR, "[data-testid='KeyboardArrowRightIcon']")
        self.left_arrow = (By.CSS_SELECTOR, "[data-testid='KeyboardArrowLeftIcon']")

        # Locators for Already exist user
        self.create_button = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button")
        self.first_name_field = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[1]/div/input")
        self.last_name_field = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input")
        self.email_field = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[3]/div/input")
        self.headquarter_dropdown = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[4]/div/div/div/button")
        self.status_toggle = (By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/label/span[1]/span[1]")
        self.submit_button = (By.XPATH, "/html/body/div[5]/div[3]/div[3]/button[2]")
        self.cancel_button = (By.XPATH, "/html/body/div[5]/div[3]/div[3]/button[1]")
        self.yes_button = (By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/button[2]")
        self.success_message = (By.XPATH, "(//div[@class='notistack-Snackbar go3963613292'])[1]")


    # Method of Create user
    def click_on_create_button(self):
        # Clicks the create button.
        create_button = self.wait.until(EC.element_to_be_clickable(self.create_btn))
        create_button.click()


    def click_on_inside_create_button(self):
        # Clicks the inside create button.
        self.driver.find_element(*self.inside_btn).click()


    # Assertions Method to get the text of an element
    def get_element_text(self, locator):
        """Gets the text of an element.
        Args:
            locator (tuple): The locator of the element (e.g., (By.ID, "element_id")).
        Returns:
            str: The text of the element, or None if the element is not found.
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            print(f"Element with locator {locator} not found within the specified time.")
            return None

    def enter_first_name(self, first_name):
        # Enters the first name in the input field.
        self.driver.find_element(*self.firstname).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Enters the last name in the input field.
        self.driver.find_element(*self.lastname).send_keys(last_name)

    def enter_email(self, email):
        # Enters the email in the input field.
        self.driver.find_element(*self.emailaddress).send_keys(email)

    def select_headquarter(self):
        # Selects a random headquarter from the dropdown.
        self.driver.find_element(*self.headquarter).click()
        options = self.driver.find_elements(*self.dropdown_options)
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options available in the dropdown.")

    def click_on_submit_btn(self):
        """Clicks the submit button."""
        self.driver.find_element(*self.submit).click()

    # def get_success_message(self):
    #     """Gets the success message text."""
    #     return self.driver.find_element(*self.success_message).text


    # Method of Edit User
    def find_first_row1(self):
        # Finds and clicks the first row in the user table.
        try:
            first_row = self.driver.find_element(By.CSS_SELECTOR, "[data-test-id*='-editicon-desktoptable-']")
            first_row.click()
            return first_row
        except Exception as e:
            print(f"Error finding first row: {e}")
            return None

    def click_on_last_name_field(self, updated_last_name):
        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.last_name_field)
        )
        last_name_field.click()

        # Clear the field properly
        last_name_field.send_keys(Keys.CONTROL, "a")  # Select all text
        last_name_field.send_keys(Keys.DELETE)
        time.sleep(1)

        # Ensure field is actually cleared
        if last_name_field.get_attribute("value"):
            self.driver.execute_script("arguments[0].value = '';", last_name_field)
        last_name_field.send_keys(updated_last_name)
        self.driver.find_element(By.TAG_NAME, "body").click()

    def click_on_edit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.edit_button)).click()

    def is_check_edit_cancel_alert_title(self, expected_text):
        return self.wait.until(EC.text_to_be_present_in_element(self.edit_cancel_alert_title, expected_text))

    def is_check_edit_cancel_alert_content(self, expected_text):
        return self.wait.until(EC.text_to_be_present_in_element(self.edit_cancel_alert_content, expected_text))

    def click_on_confirm_dialog_box(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_dialog_box)).click()

    def get_snackbar_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.edit_snackbar_message)).text


     # Method of View User
    def click_on_view_icon1(self):
        # Clicks on the view icon.
        first_row1 = self.wait.until(EC.presence_of_element_located(self.find_first_row_view_icon))
        self.wait.until(EC.element_to_be_clickable(self.find_first_row_view_icon)).click()

    def click_on_view_cross_icon(self):
        # Clicks on the view cross icon.
        self.driver.find_element(*self.cross_icon_view).click()


    # Methods of Delete User
    def click_delete_button(self):
        "Clicks the delete button on the first row."
        first_row_delete_button = self.driver.find_element(*self.delete_button)
        first_row_delete_button.click()

    def is_check_delete_alert_title(self, expected_text):
        return self.get_element_text(self.delete_alert_title) == expected_text

    def is_check_delete_alert_content(self, expected_text):
        return self.get_element_text(self.delete_alert_content) == expected_text

    def check_deleted_username(self):
        self.driver.find_element(*self.delete_username).click()

    def confirm_deletion(self):
        self.driver.find_element(*self.confirm_delete_button).click()

    def clear_previous_notifications(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.notification_message))
        except TimeoutException:
            print("No previous notifications to clear.")

    def get_notification_message2(self):
        return self.wait.until(EC.visibility_of_element_located(self.notification2)).text


    # Methods of filters
    def open_filter_dropdown(self):
        self.driver.find_element(*self.filter_dropdown).click()

    def select_option_ao(self):
        self.driver.find_element(*self.option_ao).click()

    def select_option_cl(self):
        self.driver.find_element(*self.option_cl).click()

    def close_filter_dropdown(self):
       background = self.driver.find_element(*self.close_dropdown)
       ActionChains(self.driver).move_to_element(background).click().perform()

    def click_on_clear_filters(self):
        self.driver.find_element(*self.clear_filters).click()

    def open_status_filter_dropdown(self):
         self.driver.find_element(*self.status_filter_dropdown).click()

    def select_inactive_option(self):
        self.driver.find_element(*self.inactive_option).click()


    # Methods of Search
    def get_first_row(self):
        """Waits for the table body and returns the first row element."""
        table_body_element = self.wait.until(EC.presence_of_element_located(self.table_body))
        return table_body_element.find_element(By.CSS_SELECTOR, ":first-child")

    def extract_uuid_from_row(self, first_row):
        """Extracts UUID from the first row's 'data-test-id' attribute."""
        data_test_id = first_row.get_attribute("data-test-id")
        if data_test_id is None:
            raise ValueError("No data-test-id attribute found for the first row.")

        uuid_pattern = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")
        match = uuid_pattern.search(data_test_id)
        if match:
            return match.group()
        else:
            raise ValueError(f"No valid UUID found in data-test-id: {data_test_id}")

    def get_user_name(self, first_row, uuid):
        """Retrieves the username from the first row using the extracted UUID."""
        user_name_element = first_row.find_element(
            By.CSS_SELECTOR,
            f"[data-test-id='tablebodycell-{uuid}-responsiblename-desktoptable-reinstatement-responsibles-table-list-page-reinstatement']"
        )
        user_name = user_name_element.text.strip()
        if not user_name:
            raise ValueError("User name not found in the first row.")

        return user_name

    def search_for_user_name(self, user_name):
        """Enters the username in the search input field."""
        search_bar = self.driver.find_element(*self.search_input)
        search_bar.send_keys(user_name)
        time.sleep(2)  # Consider replacing with an explicit wait

    def clear_search(self):
        """Clears the search input field."""
        clear_search = self.driver.find_element(*self.clear_search_icon)
        clear_search.click()
        time.sleep(2)  # Consider replacing with an explicit wait


    # Methods for pagination
    def is_pagination_arrow_available(self, arrow_locator):
            elements = self.driver.find_elements(*arrow_locator)
            return len(elements) > 0

    def is_pagination_arrow_enabled(self, arrow_locator):
            arrow = self.driver.find_element(*arrow_locator)
            return arrow.is_enabled() and arrow.value_of_css_property("pointer-events") == "auto"

    def click_pagination_arrow(self, arrow_locator):
            arrow = self.driver.find_element(*arrow_locator)
            arrow.click()

    def is_right_arrow_available(self):
            return self.is_pagination_arrow_available(self.right_arrow)

    def is_right_arrow_enabled(self):
            return self.is_pagination_arrow_enabled(self.right_arrow)

    def click_right_arrow(self):
            self.click_pagination_arrow(self.right_arrow)

    def is_left_arrow_available(self):
            return self.is_pagination_arrow_available(self.left_arrow)

    def is_left_arrow_enabled(self):
            return self.is_pagination_arrow_enabled(self.left_arrow)

    def click_left_arrow(self):
            self.click_pagination_arrow(self.left_arrow)


    # Methods for already user exist
    def click_create_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()

    def fill_user_details(self, first_name, last_name, email):
        self.wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(self.last_name_field)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(self.email_field)).send_keys(email)

    def select_headquarter1(self):
        # Selects a random headquarter from the dropdown.
        self.driver.find_element(*self.headquarter).click()
        options = self.driver.find_elements(*self.dropdown_options)
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options available in the dropdown.")

    def toggle_status(self):
        toggle = self.driver.find_element(*self.status_toggle)
        toggle.click()
        toggle.click()

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def click_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()

    def click_yes_button(self):
        self.wait.until(EC.element_to_be_clickable(self.yes_button)).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text

    def get_success_message1(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_message_of_createUser)).text
        except TimeoutException:
            print("Success message not found within the timeout.")
            return ""

