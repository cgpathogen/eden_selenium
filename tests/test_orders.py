import allure
from base.base_test import BaseTest

@allure.epic("Orders")
@allure.story("Orders through Catalogue")
@allure.feature("Cart")
class TestOrder(BaseTest):

    @allure.title("Place order by unauthorized user")
    def test_order_via_searching_in_catalogue(self):
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
        self.cartPage.close_advertisement()  # закрытие поп-апа с предложением
        self.cartPage.check_data_match_in_cart()
        self.cartPage.click_go_to_place_order_page()
        self.orderPage.check_products_data_match()
        self.orderPage.user_fields.enter_user_data()