import time
from pages.web.login_page import LoginPage
from config import VALID_USERNAME, VALID_PASSWORD, UNREGISTERED_EMAIL, INVALID_PASSWORD

def test_login_with_valid_credentials(driver):
    """
    Test that a user can log in with valid credentials and see the welcome back message.
    """
    login_page = LoginPage(driver)

    login_page.open()

    login_page.click_use_email_or_username()

    login_page.enter_username(VALID_USERNAME)

    login_page.click_login()

    login_page.enter_password(VALID_PASSWORD)

    login_page.click_login()

    welcome_element = login_page.wait_for_welcome_text()
    assert welcome_element.is_displayed()

def test_login_with_unregistered_email(driver):
    """
    Test login attempt with an unregistered email and verify the 'Email Not Registered' error appears.
    """
    login_page = LoginPage(driver)

    login_page.open()

    login_page.click_use_email_or_username()

    login_page.enter_username(UNREGISTERED_EMAIL)

    login_page.click_login()

    assert login_page.is_email_not_registered_displayed(), "'Email Not Registered' message not displayed"

def test_login_with_incorrect_password(driver):
    """
    Test login attempt with valid username but incorrect password and verify the 'Incorrect Password' error message appears.
    """
    login_page = LoginPage(driver)

    login_page.open()

    login_page.click_use_email_or_username()

    login_page.enter_username(VALID_USERNAME)

    login_page.click_login()

    login_page.enter_password(INVALID_PASSWORD)

    login_page.click_login()

    assert login_page.is_incorrect_password_displayed(), "'Incorrect Password' message not displayed"

def test_login_button_disabled_with_empty_email(driver):
    """
    Test that the login button is disabled when email/username field is left empty.
    """
    login_page = LoginPage(driver)

    login_page.open()

    login_page.click_use_email_or_username()


    assert login_page.is_login_button_disabled(), "Login button should be disabled when email is empty"

def test_login_button_disabled_with_empty_password(driver):
    """
    Test that the login button is disabled when password field is left empty.
    """
    login_page = LoginPage(driver)

    login_page.open()

    login_page.click_use_email_or_username()

    login_page.enter_username(VALID_USERNAME)

    login_page.click_login()


    assert login_page.is_login_button_disabled(), "Login button should be disabled when password is empty"