from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MobileLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.company_id_field = (AppiumBy.ID, "id.edot.ework.debug:id/et_company_id")
        self.username_field = (AppiumBy.ID, "id.edot.ework.debug:id/et_username")  # contoh
        self.password_field = (AppiumBy.ID, "id.edot.ework.debug:id/et_password")  # contoh
        self.login_button = (AppiumBy.ID, "id.edot.ework.debug:id/button_text")

    def login(self, company_id, username, password):
        time.sleep(5)
        print("⌛ Menunggu field ID perusahaan...")
        print(f"🔍 Mencari elemen: {self.company_id_field}")
        self.wait.until(EC.presence_of_element_located(self.company_id_field)).send_keys(company_id)

        print("🔍 Mencari username field...")
        self.wait.until(EC.presence_of_element_located(self.username_field)).send_keys(username)

        print("🔍 Mencari password field...")
        self.wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)

        print("🚀 Klik tombol login...")
        self.wait.until(EC.presence_of_element_located(self.login_button)).click()
