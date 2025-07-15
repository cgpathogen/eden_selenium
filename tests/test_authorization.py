import time
import allure
from base.base_test import BaseTest
from conftest import driver


@allure.epic("User")
@allure.story("Authorization")
class TestAuthorization(BaseTest):

    @allure.title("test chosen city is equal to the city id dropdown")
    def test_chosen_city_align(self):
        self.mainPage.open()
        self.mainPage.click_choose_no_button()
        self.mainPage.enter_text_to_search_city_input(self.mainPage.search_city_name)
        self.mainPage.choose_city_from_result()
        self.mainPage.check_city_name_align()
        time.sleep(1.5)