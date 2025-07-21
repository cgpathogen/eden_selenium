import allure
from selenium.webdriver.common.devtools.v136.input_ import DragData

from database.database import Database
from pages.base_page.base_page import BasePage
from count import count

class CartPage(BasePage):

    # locators

    ## item locators

    _item_locator = "//tr[@class='basket-items-list-item-container']"
    _item_brand_and_name_locator = "(//a[@class='basket-item-info-name-link'])"
    _item_price_locator = "(//span[@class='basket-item-price-current-text'])"
    _minus_button_locator = "//span[@class='basket-item-amount-btn-minus']"
    _plus_button_locator = "//span[@class='basket-item-amount-btn-plus']"
    _amount_locator = "(//input[@class='basket-item-amount-filed'])"

    _remove_from_cart_button = "(//div[@class='basket-item-actions-remove'])"
    _add_to_favorites_button = "(//a[@class='favorite-icon basket-item-actions-favorite h2o_add_favor'])"


    # page elements locators

    _clear_button_locator = "//input[@class='basket-coupon-clear']"
    _cart_total_price_locator = "//div[@class='basket-coupon-block-total-price-current']"
    _place_order_button_locator = "//button[@class='btn btn-lg btn-default basket-btn-checkout']"

    _close_advert_button_locator = "//*[@id='js-promo']/button"

    ## promocode
    _input_promocode_locator = "(//input[@class='form-control'])[2]"
    _apply_promocode_button_locator = "//div[@class='basket-coupon-block-coupon-btn']"
    _promocode_text_locator = "//span[@class='basket-coupon-text']"
    _remove_promocode_button_locator = "//span[@class='close-link']"

    # getters

    def get_total_price(self):
        element = self.wait_to_be_visible(self._cart_total_price_locator).text
        return self.divide_price(element)


    @allure.step("Close advertisement")
    def close_advertisement(self):
        self.wait_to_be_visible(self._close_advert_button_locator).click()

    @allure.step("Click go to cart button")
    def click_go_to_place_order_page(self):
        self.wait_to_be_clickable(self._place_order_button_locator).click()

    @allure.step("Check data match in cart")
    def check_data_match_in_cart(self):
        a = 1
        b = 2
        total = 0
        self.close_advertisement() # закрытие поп-апа с предложением
        for i in range(1, count):
            item_locator = f"{self._item_locator}[{i}]"
            self.hover(item_locator)

            # brand
            item_brand_locator = f"{self._item_brand_and_name_locator}[{i}]/span"
            item_brand = self.wait_to_be_visible(item_brand_locator).text.lower()

            # name
            item_name_locator = f"{self._item_brand_and_name_locator}[{i}]/span[2]"
            item_name = self.wait_to_be_visible(item_name_locator).text.lower()

            # price
            item_price_for_one = f"{self._item_price_locator}[{a}]"
            get_item_price = self.wait_to_be_visible(item_price_for_one).text
            item_price = self.divide_price(get_item_price)

            item_price_total = f"{self._item_price_locator}[{b}]"
            get_item_price_total = self.wait_to_be_visible(item_price_total).text
            item_price_total = self.divide_price(get_item_price_total)

            total_item_count = f"{self._amount_locator}[{i}]"
            get_total_item_count = int(self.wait_to_be_visible(total_item_count).get_attribute("value"))

            assert Database.select_item_data(i)[0] == item_brand
            assert Database.select_item_data(i)[1] == item_name
            assert item_price * get_total_item_count == item_price_total
            total += item_price_total
        assert total == self.get_total_price() # финальная сверка общей цены с суммой за каждый товар в корзине