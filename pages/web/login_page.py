from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import VALID_USERNAME, VALID_PASSWORD

class LoginPage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.url = "https://esuite.edot.id"
        self.wait = WebDriverWait(driver, timeout)

    # Locators
    use_email_button = (By.XPATH, "//button[contains(., 'Use Email or Username')]")
    username_input = (By.NAME, "username")
    login_button = (By.XPATH, "//button[contains(., 'Log In')]")
    password_input = (By.NAME, "password")
    welcome_text = (By.XPATH, "//span[text()='Welcome Back,']")
    email_not_registered_error = (By.XPATH, "//p[text()='Email Not Registered']")
    incorrect_password_error = (By.XPATH, "//p[contains(@class, 'text-red-500') and contains(text(), 'Incorrect password')]")

    # Actions
    def open(self):
        self.driver.get(self.url)

    def click_use_email_or_username(self):
        self.wait.until(EC.element_to_be_clickable(self.use_email_button)).click()

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        field.clear()
        field.send_keys(username)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        field.clear()
        field.send_keys(password)

    def wait_for_welcome_text(self, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.welcome_text)
        )
    
    def is_email_not_registered_displayed(self, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.email_not_registered_error)
        )
    
    def is_incorrect_password_displayed(self, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.incorrect_password_error)
        )
    
    def is_login_button_disabled(self):
        login_button = self.wait.until(EC.presence_of_element_located(self.login_button))
        return login_button.get_attribute("disabled") == "true"
    
    def do_login(self, username=VALID_USERNAME, password=VALID_PASSWORD):
        self.open()
        self.click_use_email_or_username()
        self.enter_username(username)
        self.click_login()
        self.enter_password(password)
        self.click_login()
        self.wait_for_welcome_text()
