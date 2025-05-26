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
- Docker for containerization
- noVNC for browser visualization

---

## Features Covered
- Login user
- Create user
- Edit user
- View user details
- Delete user
- Search user by name
- Filter/search users (by Headquarter and Status)
- Pagination testing
- Check for already existing users

---

## Running Tests with Docker and noVNC

This setup allows you to run Selenium tests with a visible Chrome browser through noVNC.

### Prerequisites

1. Docker installed on your machine
2. Docker Compose installed on your machine
3. Internet connection to access the application at `https://reinstatements-delegations-reinstatement-responsg-iymj66chvq-uc.a.run.app/`

### Automated Setup (Recommended)

Run the automated script to start the containers and open the noVNC viewer:

```bash
./run_tests_with_novnc.sh
```

This script will:
1. Stop any running containers
2. Start the Chrome container with noVNC
3. Open the noVNC viewer in your default browser with auto-connect enabled
4. Run the test cases automatically
5. Show the logs

The noVNC viewer will automatically connect to the Chrome browser without requiring a password, and the test cases will run automatically in the browser window.

### Manual Setup

If you prefer to run the commands manually:

1. Start the Chrome container:
   ```bash
   docker compose up -d chrome
   ```

2. Access the noVNC browser:
   - Open your web browser and go to http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=
   - This URL will automatically connect to the Chrome browser without requiring a password

3. To run tests, use the following command:
   ```bash
   docker compose run --rm selenium-tests
   ```

4. To stop the containers:
   ```bash
   docker compose down
   ```

### Docker Configuration

The project uses a Docker setup with two main services:

1. **chrome**: Runs the Selenium standalone Chrome container with noVNC for visual debugging
2. **selenium-tests**: Runs the test scripts against the Chrome container

The tests connect to the application at `https://reinstatements-delegations-reinstatement-responsg-iymj66chvq-uc.a.run.app/`.

### Troubleshooting

1. **Network Issues**: If the tests can't connect to the application, check your internet connection and make sure the URL is accessible.

2. **noVNC Access Issues**: If you can't access the noVNC viewer at http://localhost:7900:
   - Check if the ports are correctly mapped with `docker ps`
   - Make sure no other application is using port 7900

3. **Google Login Issues**: The tests may have issues with Google login. You may need to:
   - Manually interact with the Google login page when it appears
   - Wait for the login process to complete before the tests continue

4. **Container Startup Issues**: If the Chrome container fails to start:
   - Check Docker logs with `docker compose logs chrome`
   - Ensure you have enough system resources (memory, CPU) available

---

## Local Development Setup

If you prefer to run the tests locally without Docker:

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/reinstatement-automation.git
   cd reinstatement-automation
   ```

2. Configure Project Settings:
   Open the config/config.py file and set the following values:
   ```bash
     a.  base_url: Set to "https://reinstatements-delegations-reinstatement-responsg-iymj66chvq-uc.a.run.app/"
     b.  language: Choose the testing language ("en_US" for English or "Español" for Spanish, etc.).
     c.  email and password: Provide valid login credentials for the platform.
   ```

3. Install Required Dependencies:
   ```bash
   pip install -r requirements.txt
   pip install webdriver-manager pytest-html
   ```

4. Run the Automation:
   ```bash
   # Run all tests
   pytest -v main_driver.py

   # Run a specific test
   pytest -v main_driver.py::test_create_user
   ```

5. Notes for Local Testing:
   - You'll need Chrome browser installed on your machine
   - The webdriver-manager package will automatically download the appropriate ChromeDriver version
   - You may need to manually interact with the Google login page when it appears
