import pytest
from pages.web.login_page import LoginPage
from pages.web.company_page import CompanyPage
import time

def test_add_company_with_valid_input(web_driver):
    login_page = LoginPage(web_driver)
    company_page = CompanyPage(web_driver)

    login_page.do_login()

    company_page.go_to_companies_menu()

    company_page.click_add_company()

    company_data = {
        "company_name": "PT ABC",
        "email": "abc@xyz.com",
        "phone": "081234567890",
        "industry_type": "Technology",
        "company_type": "Service Provider",
        "language": "English",
        "street_address": "Jl Dang Merdu",
        "country": "Indonesia",
        "province": "KEP RIAU",
        "city": "KOTA BATAM",
        "district": "BATAM KOTA",
        "subdistrict": "BELIAN"
    }
    company_page.fill_company_form(company_data)

    filled_data = company_page.get_filled_company_form_data()

    company_page.click_next_button()
    assert company_page.is_next_step_after_register_company()

    company_page.click_next_button()
    assert company_page.is_next_step_after_register_legalbank()

    time.sleep(3)
    company_page.click_fill_with_company_data()
    company_page.click_agree_policy_checkbox()
    company_page.click_register_button()

    company_page.click_manage_button_for_company(company_data["company_name"])

    assert filled_data["company_name"] == company_data["company_name"]
    assert filled_data["email"]        == company_data["email"]
    assert filled_data["phone"]        == company_data["phone"]
    assert filled_data["address"]      == company_data["street_address"]

def test_leave_all_fields_empty(web_driver):
    login_page = LoginPage(web_driver)
    company_page = CompanyPage(web_driver)

    login_page.do_login()

    company_page.go_to_companies_menu()

    company_page.click_add_company()

    assert company_page.is_next_button_disabled(), "Next button should be disabled when all required fields are empty"

def test_enter_invalid_email_format(web_driver):
    login_page = LoginPage(web_driver)
    company_page = CompanyPage(web_driver)

    login_page.do_login()

    company_page.go_to_companies_menu()

    company_page.click_add_company()

    company_page.fill_company_form({
        "company_name": "PT ABC",
        "email": "abc@xyz",
        "phone": "081234567890",
        "industry_type": "Technology",
        "company_type": "Service Provider",
        "language": "English",
        "street_address": "Jl Dang Merdu",
        "country": "Indonesia",
        "province": "KEP RIAU",
        "city": "KOTA BATAM",
        "district": "BATAM KOTA",
        "subdistrict": "BELIAN"
    })

    company_page.click_next_button()

    assert company_page.is_invalid_email_message_displayed(), "Expected error for invalid email format not displayed"

