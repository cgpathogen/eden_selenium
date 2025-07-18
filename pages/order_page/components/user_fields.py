import allure
from pages.base_page.base_page import BasePage

class UserFields(BasePage):

    # locators

    _name_input_locator = "//input[@id='soa-property-27']"
    _phone_input_locator = "//input[@id='soa-property-29']"
    _email_input_locator ="//input[@id='soa-property-26']"
    _address_input_locator = "//textarea[@id='soa-property-38']"
    _comment_input_locator = "//textarea[@id='orderDescription']"