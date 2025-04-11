import os
import time
from Page_Functions.login_page_function import TestLogin
from Page_Functions.create_user_page_function import CreateUserTest
import Page_Functions.create_user_page_function
from config.config import Config

class MainDriverClass:
    driver = None

    @classmethod
    def setup_language(cls):
        print(f"Running tests in language: {Config.language}")
        os.environ["TEST_LANGUAGE"] = Config.language

    @classmethod
    def run(cls):
        # Main method to execute tests.
        print("Starting main method...")

        # Initialize and execute login test
        login_test = TestLogin()
        login_test.setup_method()
        cls.driver = login_test.driver
        login_test.test_login_user()
        print("User login successful.")

        if cls.driver is None:
            print("Error: WebDriver is not initialized. Exiting...")
            return

        # Initialize CreateUserTest
        create_user_test = CreateUserTest()

        # Run create user management tests
        create_user_test.create_user()
        time.sleep(2)
        print("user create successfully")

        # Run edit user test
        create_user_test.test_edit_user()
        print ("Edit information of user successfully")

        # Run View user test
        create_user_test.test_view_user()
        time.sleep(2)
        print("View information successfully")

        # Run delete user test
        create_user_test.test_delete_user()
        time.sleep(2)
        print("User deleted successfully")

        # Run filter user test
        create_user_test.test_filter_functionality()
        time.sleep(2)
        print("Headquarter and Status filter working successfully")

        # Run for pagination of user test
        create_user_test.test_pagination()
        time.sleep(2)
        print("Pagination is working successfully")

        # Run Already exist user
        create_user_test.test_already_exist_user()
        time.sleep(2)
        print("User already exist")

        print("Main method execution complete.")

if __name__ == "__main__":
    MainDriverClass.setup_language()
    MainDriverClass.run()


