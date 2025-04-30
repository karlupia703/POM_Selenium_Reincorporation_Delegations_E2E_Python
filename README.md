


# Reincorporation Delegations Project (Python + Selenium)

## Overview
This automation project uses **Selenium WebDriver** with **Python** and **PyTest** to test the functionality of the **Reinstatement Platform**.  
It includes test cases for user management: login, create/edit/delete users, filter, pagination, and verifying duplicate users.

---

## Tech Stack
- Python 3.x
- Selenium
- PyTest
- PyTest Fixtures
- HTML Reporting (optional: `pytest-html`)
- POM (Page Object Model) Design Pattern

---

## Features Covered
- Login user
- Create user
- Edit user
- View user details
- Delete user
- Filter/search users (by Headquarter and Status)
- Pagination testing
- Check for already existing users

---

## Configuration Setup

1. Clone the Repository:
   ```bash   
   git clone https://github.com/your-username/reinstatement-automation.git
   cd reinstatement-automation
   ```

2. Configure Project Settings:

   Open the config/config.py file and set the following values: 
   ```bash
     a.  base_url: Add the URL where the front-end of the website is running.
     b.  language: Choose the testing language ("en_US" for English or "Español" for Spanish, etc.).
     c.  email and password: Provide valid login credentials for the platform.
     Most of the basic setup has already been done. You just need to update the essential values above before running the tests.
   ```

3. Install Required Dependencies:
   ```bash
   pip install -r requirements.txt
    ```

4. Verify Configuration:
   
   Ensure config/config.py contains valid values. This file drives environment-specific behavior.
   ```bash
   Make sure all required fields are correctly set in config.py.
   Once confirmed, you're ready to start running test cases.
   ```

5. Run the Automation:

   Once everything is properly configured in config/config.py, start the test execution using:
   ```bash
    pytest -v main_driver.py
    ```

6. View and Export Logs (Recommended for PyCharm Users):
 
   After test execution:
    
   - Go to the Run tab in PyCharm.
   - Click on the More button (three dots).
   - Select Export Test Results.
   - Choose the path where you want to save the log file.
   - Once saved, right-click the file and open it in a browser to review.
    