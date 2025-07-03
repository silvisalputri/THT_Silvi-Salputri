from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class CompanyPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # === Locators ===
    companies_menu = (By.XPATH, "//a[@href='/companies']")
    add_company_button = (By.XPATH, "//button[contains(.,'Add Company')]")
    company_name_input = (By.XPATH, "//input[@placeholder='Input Company Name']")
    email_input = (By.XPATH, "//input[@placeholder='Input Email']")
    phone_input = (By.XPATH, "//input[@placeholder='Input Phone']")
    street_address_input = (By.XPATH, "//input[@placeholder='Input Address']")
    next_button = (By.XPATH, "//button[contains(.,'Next')]")
    company_profile_header = (By.XPATH, "//h2[contains(text(),'Company Profile')]")
    my_company_header = (By.XPATH, "//*[contains(text(),'My Company')]")
    register_company_header = (By.XPATH, "//*[contains(text(),'Register Company')]")
    register_legal_bank_header = (By.XPATH, "//*[contains(text(),'Register Legal & Bank')]")
    create_branch_header = (By.XPATH, "//*[contains(text(),'Create Your Branch')]")
    invalid_email_format_message = (By.XPATH, "//span[contains(text(), 'Please provide a valid email address')]")
    agree_policy_checkbox = (By.ID, "select-all")
    register_button = (By.XPATH, "//button[normalize-space(text())='Register']")
    fill_with_company_data_button = (By.XPATH,"//button[normalize-space(text())='Fill in with the same data from the Company records']")

    # === Page Actions ===
    def go_to_companies_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.companies_menu)).click()
        self.wait.until(EC.visibility_of_element_located(self.my_company_header))

    def click_add_company(self):
        self.wait.until(EC.element_to_be_clickable(self.add_company_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.register_company_header))

    def fill_company_form(self, data):
        self.wait.until(EC.visibility_of_element_located(self.company_name_input)).send_keys(data["company_name"])
        self.driver.find_element(*self.email_input).send_keys(data["email"])
        self.driver.find_element(*self.phone_input).send_keys(data["phone"])
        self.select_custom_dropdown("Choose Industry Type", data["industry_type"])
        self.select_custom_dropdown("Choose Company Type", data["company_type"])
        self.select_custom_dropdown("Choose Language", data["language"])
        self.driver.find_element(*self.street_address_input).send_keys(data["street_address"])
        self.select_custom_dropdown("Choose Country", data["country"])
        self.select_custom_dropdown("Choose Province", data["province"])
        self.select_custom_dropdown("Choose City", data["city"])
        self.select_custom_dropdown("Choose District", data["district"])
        self.select_custom_dropdown("Choose Sub District", data["subdistrict"])

    def select_custom_dropdown(self, label_text, option_text):
        dropdown_xpath = f"//button[@role='combobox' and .//span[text()='{label_text}']]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath))).click()
        option_xpath = f"//div[contains(@class, 'cursor-default')]//span[text()='{option_text}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()

    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

    def is_next_step_after_register_company(self):
        return self.wait.until(EC.visibility_of_element_located(self.register_legal_bank_header)).is_displayed()
    
    def is_next_step_after_register_legalbank(self):
        return self.wait.until(EC.visibility_of_element_located(self.create_branch_header)).is_displayed()

    def click_agree_policy_checkbox(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(self.agree_policy_checkbox))
        checkbox.click()

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button)).click()

    def click_manage_button_for_company(self, company_name):
        # Gunakan pendekatan lebih fleksibel
        manage_button_xpath = f"//div[text()='{company_name}']/following::button[normalize-space(text())='Manage'][1]"
        manage_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, manage_button_xpath)))
        manage_button.click()

    def open_company_detail(self, company_name):
        row = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//td[contains(text(), '{company_name}')]")))
        row.click()

    def get_input_value(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute("value")

    def get_filled_company_form_data(self):
        return {
            "company_name": self.get_input_value(self.company_name_input),
            "email": self.get_input_value(self.email_input),
            "phone": self.get_input_value(self.phone_input),
            "address": self.get_input_value(self.street_address_input),
        }

    def is_invalid_email_message_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.invalid_email_format_message)).is_displayed()
        except:
            return False
    
    def click_fill_with_company_data(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.fill_with_company_data_button)
        )
        btn.click()

