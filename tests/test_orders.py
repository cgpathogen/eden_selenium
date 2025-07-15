import time
import allure
from base.base_test import BaseTest

@allure.epic("Orders")
@allure.feature("Place order by authorized user")
class TestOrder(BaseTest):

    @allure.title("Order via searching in catalogue")
    def test_order_via_searching_in_catalogue(self):
        self.mainPage.open()
        self.mainPage.click_choose_yes_button() # скрываем поп-ап с выбором города, который перекрывает кнопку каталога
        self.mainPage.hover_catalogue_button()
        self.mainPage.hover_link_in_catalogue_1st_lvl(3) # -> парфюмерия
        self.mainPage.hover_link_in_catalogue_2st_lvl(2,True) # -> мужская парфюмерия
        time.sleep(5)