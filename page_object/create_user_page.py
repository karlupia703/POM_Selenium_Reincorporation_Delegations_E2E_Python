import string
import time
import random
import re
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

class CreateUserPages:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Initialize WebDriverWait

    # Using element location for create user
    create_btn = By.CSS_SELECTOR, "[data-test-id='button-responsibleform-create']"
    inside_btn = By.CSS_SELECTOR, "[data-test-id='custombtn-modal-responsibleform-create-submit']"
    firstname = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[1]/div/input"
    lastname = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input"
    email_address = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[3]/div/input"
    headquarter = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[4]/div/div/div/button"
    dropdown_options = By.XPATH, "//ul[@role='listbox']/li"
    submit = By.CSS_SELECTOR, "[data-test-id='custombtn-modal-responsibleform-create-submit']"

    # For Assertions
    first_name_error = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[1]/p"
    last_name_error = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/p"
    email_error = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[3]/p"
    headquarter_error = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[4]/div/p"
    success_message = By.CSS_SELECTOR, "div[id='notistack-snackbar'] div[class='MuiBox-root mui-0']"

    # Using element location for edit user
    find_first_row = By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(5) div:nth-child(1) button:nth-child(2) svg"
    last_name_field = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input"
    clear_last_name = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[2]/div/input"
    edit_button = By.XPATH, "/html/body/div[5]/div[3]/div[3]/button[2]"
    confirm_dialog_box = By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/button[2]"
    edit_cancel_alert_title = By.CSS_SELECTOR, "[data-test-id='dialogBox-title-alertBox-responsiblitiesform-edit']"
    edit_cancel_alert_content = By.CSS_SELECTOR, "[data-test-id='dialogBox-content-alertBox-responsiblitiesform-edit']"
    edit_snackbar_message = By.XPATH, "(//div[@class='notistack-Snackbar go3963613292'])[1]"

    # Using element location for view user
    find_first_row_view_icon = By.CSS_SELECTOR, "[data-test-id*='-viewicon-desktoptable-']"
    cross_icon_view = By.CSS_SELECTOR, "[data-test-id='customdialog-canclebtn-view-viewresponsible-reinstatement-responsibles-table-list-page-reinstatement']"

    # Using element location for delete user
    delete_button = By.CSS_SELECTOR, "[data-test-id*='-deleteicon-desktoptable-']"
    confirm_delete_button = By.CSS_SELECTOR, "[data-test-id='custombtn-dialogBox-submit-alertbox-delete-reinstatement-responsibles-table-list-page-reinstatement']"
    notification_message = By.CSS_SELECTOR, "#notistack-snackbar .MuiBox-root"
    delete_alert_title = By.XPATH, "/html/body/div[5]/div[3]/div/h2"
    delete_alert_content = By.CSS_SELECTOR, "[data-test-id='alertbox-deletetext-reinstatement-responsibles-table-list-page-reinstatement']"
    delete_username = By.CSS_SELECTOR, "[data-test-id='alertbox-deleteusername-reinstatement-responsibles-table-list-page-reinstatement']"
    notification2 = By.CSS_SELECTOR, "#notistack-snackbar > .MuiBox-root"

    # Using element location for search user
    table_body = By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/table/tbody"
    search_input = By.XPATH, "//input[@placeholder='Search responsible' or @placeholder='Buscar Responsable' or @placeholder='Cerca responsabile' or @placeholder='Pesquisar responsável']"
    clear_search_icon = (By.CSS_SELECTOR, "[data-test-id='icon-clear-searchbar-page-reinstatement']")

    # Using element location for test filter
    headquarter_dropdown_filter = By.CSS_SELECTOR, "[data-test-id='chip-label-autocompletefilter-destop-filter-headquarter-page-reinstatement']"
    headquarter_list = By.XPATH, "/html/body/div[5]/div[3]/div[2]/ul/li"
    option_ao = By.CSS_SELECTOR, "[data-test-id='list-item-AO-autocompletefilter-destop-filter-headquarter-page-reinstatement']"
    option_cl = By.CSS_SELECTOR, "[data-test-id='list-item-CL-autocompletefilter-destop-filter-headquarter-page-reinstatement']"
    close_dropdown = By.TAG_NAME, "body"
    clear_filters = By.CSS_SELECTOR, "[data-test-id='clear-btn-header-page-reinstatement']"
    status_filter = By.CSS_SELECTOR, "[data-test-id='label-render-value-filter-status-page-reinstatement']"
    status_filter_dropdown = By.XPATH, "/html/body/div[5]/div[3]/ul/li"

    # Locators for pagination
    right_arrow = (By.CSS_SELECTOR, "[data-testid='KeyboardArrowRightIcon']")
    left_arrow = (By.CSS_SELECTOR, "[data-testid='KeyboardArrowLeftIcon']")

    # Locators for Already exist user
    create_button = By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button"
    first_name_field = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[1]/div/input"
    email_field = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[3]/div/input"
    headquarter_dropdown = By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/form/div[4]/div/div/div/button"
    status_toggle = By.CSS_SELECTOR, "[data-test-id='input-responsibleswitch-responsibleform-create']"
    submit_button = By.CSS_SELECTOR, "[data-test-id='custombtn-modal-responsibleform-create-submit']"
    cancel_button = By.CSS_SELECTOR, "[data-test-id='modal-cancelaction-responsibleform-create']"
    yes_button = By.CSS_SELECTOR, "[data-test-id='custombtn-dialogBox-submit-alertBox-responsibleform-create']"
    success_message_of_createUser = (By.CSS_SELECTOR, "#notistack-snackbar .MuiBox-root")
    email_already_exist_toster_msg = By.CSS_SELECTOR, "div[id='notistack-snackbar'] div[class='MuiBox-root mui-0']"


    # Method of Create user
    def click_on_create_button(self):
        create_button = self.wait.until(EC.element_to_be_clickable(self.create_btn))
        create_button.click()

    def click_on_inside_create_button(self):
        self.driver.find_element(*self.inside_btn).click()

    # Assertions Method to get the text of an element
    def get_element_text(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            print(f"Element with locator {locator} not found within the specified time.")
            return None

    # Method to assert  text
    def is_first_name_error_text(self, expected_text):
        """Checks if the first name error text matches the expected text."""
        return self.get_element_text(self.first_name_error) == expected_text

    def is_last_name_error_text(self, expected_text):
        """Checks if the last name error text matches the expected text."""
        return self.get_element_text(self.last_name_error) == expected_text

    def is_email_error_text(self, expected_text):
        """Checks if the email field error text matches the expected text."""
        return self.get_element_text(self.email_error) == expected_text

    def is_headquarter_error_text(self, expected_text):
        """Checks if the headquarter error text matches the expected text."""
        return self.get_element_text(self.headquarter_error) == expected_text


    def enter_first_name(self, first_name):
        # Enters the first name in the input field.
        self.driver.find_element(*self.firstname).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Enters the last name in the input field.
        self.driver.find_element(*self.lastname).send_keys(last_name)

    def enter_email(self, email):
        # Enters the email in the input field.
        self.driver.find_element(*self.email_address).send_keys(email)

    def select_headquarter(self):
        # Selects a random headquarters from the dropdown.
        self.driver.find_element(*self.headquarter).click()
        options = self.driver.find_elements(*self.dropdown_options)
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options available in the dropdown.")

    def click_on_submit_btn(self):
        self.driver.find_element(*self.submit).click()

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
        last_name_field.send_keys(Keys.CONTROL, "a")
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
        self.wait.until(EC.element_to_be_clickable(self.find_first_row_view_icon)).click()

    def click_on_view_cross_icon(self):
        self.driver.find_element(*self.cross_icon_view).click()


    # Methods of Delete User
    def click_delete_button(self):
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


    # Methods of Search
    def get_first_row(self):
        table_body_element = self.wait.until(EC.presence_of_element_located(self.table_body))
        return table_body_element.find_element(By.CSS_SELECTOR, ":first-child")

    def extract_uuid_from_row(self, first_row):
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
        user_name_element = first_row.find_element(
            By.CSS_SELECTOR,
            f"[data-test-id='tablebodycell-{uuid}-responsiblename-text-desktoptable-reinstatement-responsibles-table-list-page-reinstatement']"
        )
        user_name = user_name_element.text.strip()
        if not user_name:
            raise ValueError("User name not found in the first row.")
        return user_name

    def search_for_user_name(self, user_name):
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_input)
        )
        search_bar.send_keys(user_name)

    def clear_search(self):
        clear_search = self.driver.find_element(*self.clear_search_icon)
        clear_search.click()

    def search_with_random_text_and_check_no_results(self):
        # Generate random search text
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        search_field_element = self.driver.find_element(*self.search_input)
        search_field_element.click()
        search_field_element.send_keys(random_text)
        time.sleep(2)
        # Check for 'No results found' message
        try:
            no_result_element = self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='nocontentheading-tablenocontent-desktoptable-reinstatement-responsibles-table-list-page-reinstatement']")
            if no_result_element.is_displayed():
                print(f"Message displayed: 'No results found' for search '{random_text}'")
            else:
                print("No results found' message is not visible.")
        except:
            print("No results found' element not found. Maybe results are unexpectedly present.")

        self.driver.find_element(*self.clear_search_icon).click()


    # Methods of filters
    def open_filter_dropdown(self):
        self.driver.find_element(*self.headquarter_dropdown_filter).click()

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
        self.driver.find_element(*self.status_filter).click()
        options = self.driver.find_elements(*self.status_filter_dropdown)
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options available in the dropdown.")
            time.sleep(3)


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

    def get_email_already_exist_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.email_already_exist_toster_msg)).text