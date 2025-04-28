import os
import time
import pytest
from page_functions.login_page_function import TestLogin
from page_functions.create_user_page_function import CreateUserTest
from config.config import Config

def test_setup_language():
    print(f"Running tests in language: {Config.language}")
    os.environ["TEST_LANGUAGE"] = Config.language

@pytest.fixture(scope="module")
def reinstatement_page():
        login_test = TestLogin()
        login_test.setup_method()
        login_test.test_login_user()
        print("User login successful.")

        # Initialize CreateUserTest
        user = CreateUserTest()
        user.driver = login_test.driver
        return user

# Run create user management tests
def test_create_user(reinstatement_page):
        reinstatement_page.create_user()
        print("user create successfully")

# Run edit user test
def test_edit_user(reinstatement_page):
        reinstatement_page.test_edit_user()
        time.sleep(2)
        print("Edit information of user successfully")

# Run View user test
def test_view_user(reinstatement_page):
        reinstatement_page.test_view_user()
        time.sleep(2)
        print("View information successfully")

# Run delete user test
def test_delete_user(reinstatement_page):
        reinstatement_page.test_delete_user()
        time.sleep(2)
        print("User deleted successfully")

# Run filter user test
def test_filter_functionality(reinstatement_page):
        reinstatement_page.test_filter_functionality()
        time.sleep(2)
        print("Headquarter and Status filter working successfully")

# Run for pagination of user test
def test_pagination(reinstatement_page):
        reinstatement_page.test_pagination()
        time.sleep(2)
        print("Pagination is working successfully")

# Run Already exist user
def test_already_exist_user(reinstatement_page):
        reinstatement_page.test_already_exist_user()
        time.sleep(2)
        print("User already exist")