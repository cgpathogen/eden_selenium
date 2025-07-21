import time
import allure
from base.base_test import BaseTest


@allure.epic("User")
@allure.story("Authorization")
class TestAuthorization(BaseTest):

    @allure.title("test authorization as registered user")
    def test_login_logout_as_registered_user(self):
        self.mainPage.open()
        self.mainPage.click_enter_button()
        self.mainPage.auth_enter_email(self.credentials.login)
        self.mainPage.auth_enter_password(self.credentials.password)
        self.mainPage.auth_click_enter_button()
        self.mainPage.click_enter_button()
        assert self.credentials.login == self.personalCabinetPage.get_username_text()
        self.personalCabinetPage.nav_links.click_logout_link()
        self.mainPage.click_enter_button()
        self.mainPage.get_popup_title()
        time.sleep(1.5)


    @allure.title("test authorization without login")
    def test_authorization_without_login(self):
        self.mainPage.open()
        self.mainPage.click_enter_button()
        self.mainPage.auth_enter_password(self.credentials.password)
        self.mainPage.auth_click_enter_button()
        self.mainPage.click_enter_button()
        self.mainPage.get_incorrect_data_message_text()


    @allure.title("test authorization with wrong password")
    def test_authorization_with_wrong_password(self):
        self.mainPage.open()
        self.mainPage.click_enter_button()
        self.mainPage.auth_enter_email(self.credentials.login)
        self.mainPage.auth_enter_password(self.credentials.password+"test")
        self.mainPage.auth_click_enter_button()
        self.mainPage.click_enter_button()
        self.mainPage.get_incorrect_data_message_text()


    @allure.step("test authorization with password which's letters are in one register")
    def test_authorization_with_password_in_same_register(self):
        self.mainPage.open()
        self.mainPage.click_enter_button()
        self.mainPage.auth_enter_email(self.credentials.login)
        self.mainPage.auth_enter_password(self.credentials.password)
        self.mainPage.auth_click_enter_button()
        self.mainPage.click_enter_button()
        self.mainPage.get_incorrect_data_message_text()


    @allure.step("test authorization with empty inputs")
    def test_authorization_with_empty_inputs(self):
        self.mainPage.open()
        self.mainPage.click_enter_button()
        self.mainPage.auth_click_enter_button()
        self.mainPage.click_enter_button()
        self.mainPage.get_incorrect_data_message_text()