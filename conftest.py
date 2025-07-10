import pytest
import os
from selenium import webdriver
from appium import webdriver as appium_webdriver
from pages.web.login_page import LoginPage
from pages.mobile.mobile_login_page import MobileLoginPage
from config import VALID_USERNAME, VALID_PASSWORD, VALID_COMPANY_ID
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# === WEB FIXTURES ===
@pytest.fixture(scope="function")
def driver():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_web_driver():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_use_email_or_username()
    login_page.enter_username(VALID_USERNAME)
    login_page.click_login()
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()
    login_page.wait_for_welcome_text()

    yield driver
    driver.quit()


# === MOBILE FIXTURES ===
@pytest.fixture(scope="function")
def mobile_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "2b7e450e",  # device real kamu
        "app": os.path.abspath("apps/ework_1.20.5.apk"),
        "appPackage": "id.edot.ework.debug",
        "appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
        "automationName": "UiAutomator2",
        "ignoreHiddenApiPolicyError": True,
        "autoGrantPermissions": True,
        "noReset": True
    }
    driver = appium_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_mobile_driver(mobile_driver):
    login_page = MobileLoginPage(mobile_driver)
    login_page.login(VALID_COMPANY_ID, VALID_USERNAME, VALID_PASSWORD)
    yield mobile_driver