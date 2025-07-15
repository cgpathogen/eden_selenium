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