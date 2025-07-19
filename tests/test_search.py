import time
import allure
from base.base_test import BaseTest

@allure.epic("Orders")
@allure.story("Search")
class TestSearch(BaseTest):

    @allure.title("Check popular request in all items' names in catalogue")
    def test_request_in_item_name(self):
        self.mainPage.open()
        self.mainPage.click_choose_yes_button()
        self.cataloguePage.click_catalogue_button()
        self.cataloguePage.parse_items_data()
        time.sleep(2)