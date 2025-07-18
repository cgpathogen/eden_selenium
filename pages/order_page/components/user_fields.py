import allure
from pages.base_page.base_page import BasePage
from faker import Faker

class UserFields(BasePage):

    faker = Faker("ru_RU")

    # locators

    _name_input_locator = "//input[@id='soa-property-27']"
    _phone_input_locator = "//input[@id='soa-property-29']"
    _email_input_locator ="//input[@id='soa-property-26']"
    _address_input_locator = "//textarea[@id='soa-property-38']"
    _comment_input_locator = "//textarea[@id='orderDescription']"

    @allure.step("enter user name")
    def enter_user_name(self):
        self.wait_to_be_clickable(self._name_input_locator).send_keys(f"{self.faker.first_name()} {self.faker.last_name()}")

    @allure.step("enter user phone")
    def enter_user_phone(self):
        self.wait_to_be_clickable(self._phone_input_locator).send_keys(self.faker.phone_number())

    @allure.step("enter user email")
    def enter_user_email(self):
        self.wait_to_be_clickable(self._email_input_locator).send_keys(self.faker.email())

    @allure.step("enter user address")
    def enter_user_address(self):
        self.wait_to_be_clickable(self._address_input_locator).send_keys(self.faker.address())

    @allure.step("leave comment")
    def leave_comment(self):
        self.wait_to_be_clickable(self._comment_input_locator).send_keys(self.faker.text())


    @allure.title("Enter user data")
    def enter_user_data(self):
        self.enter_user_name()
        self.enter_user_phone()
        self.enter_user_email()
        self.enter_user_address()
        self.leave_comment()