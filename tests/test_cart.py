import time
import allure
from base.base_test import BaseTest

@allure.title("Orders")
@allure.story("Orders through Catalogue")
@allure.feature("Cart")
class TestCart(BaseTest):

    @allure.title("test removing products from cart")
    def test_removing_items_from_cart(self):
        self.mainPage.open()
        self.mainPage.click_choose_yes_button() # скрываем поп-ап с выбором города, который перекрывает кнопку каталога
        self.mainPage.hover_catalogue_button()
        self.mainPage.hover_link_in_catalogue_1st_lvl(3) # -> парфюмерия
        self.mainPage.hover_link_in_catalogue_2st_lvl(2,True) # -> мужская парфюмерия
        self.cataloguePage.filters.click_sort_options_dropdown()
        self.cataloguePage.filters.click_sort_by_price_asc()
        self.cataloguePage.filters.enter_min_price(1000)
        self.cataloguePage.filters.enter_max_price(1100)
        self.cataloguePage.filters.click_show_results_by_price_btn()
        self.cataloguePage.add_goods_to_cart() # алгоритм добавления товаров в корзину
        self.cataloguePage.click_cart_button()
        self.cartPage.close_advertisement()
        self.cartPage.remove_items_from_cart()