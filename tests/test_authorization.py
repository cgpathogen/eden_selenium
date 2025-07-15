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


    @allure.title("test chosen city is equal to the city id dropdown")
    def test_chosen_city_align(self):
        self.mainPage.open()
        self.mainPage.click_choose_no_button()
        self.mainPage.enter_text_to_search_city_input(self.mainPage.search_city_name)
        self.mainPage.choose_city_from_result()
        self.mainPage.check_city_name_align()
        time.sleep(1.5)