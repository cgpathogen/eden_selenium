import allure
from base.base_test import BaseTest

@allure.epic("Orders")
@allure.feature("Place order by unauthorized user")
class TestOrder(BaseTest):

    @allure.title("Order via searching in catalogue")
    def test_order_via_searching_in_catalogue(self):
        self.mainPage.open()
        self.mainPage.click_choose_yes_button() # скрываем поп-ап с выбором города, который перекрывает кнопку каталога
        self.mainPage.hover_catalogue_button()
        self.mainPage.hover_link_in_catalogue_1st_lvl(3) # -> парфюмерия
        self.mainPage.hover_link_in_catalogue_2st_lvl(2,True) # -> мужская парфюмерия
        self.cataloguePage.filters.click_sort_options_dropdown()
        self.cataloguePage.filters.click_sort_by_price_asc()
        self.cataloguePage.filters.enter_min_price(900)
        self.cataloguePage.filters.enter_max_price(2250)
        self.cataloguePage.filters.click_show_results_by_price_btn()
        self.cataloguePage.add_goods_to_cart() # алгоритм добавления товаров в корзину
        self.cataloguePage.click_cart_button()
        self.cartPage.check_data_match_in_cart()
        self.cartPage.click_go_to_cart_button()
        self.orderPage.check_products_data_match()
        self.orderPage.user_fields.enter_user_data()