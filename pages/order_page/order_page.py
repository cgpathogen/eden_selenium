import allure
import math

from count import count
from database.database import Database
from pages.base_page.base_page import BasePage
from pages.order_page.components.delivery_region import DeliveryRegion
from pages.order_page.components.delivery_service import DeliveryService
from pages.order_page.components.user_fields import UserFields

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.delivery_region = DeliveryRegion(driver)
        self.delivery_service = DeliveryService(driver)
        self.user_fields = UserFields(driver)


    # locators

    _item_name_locator = "(//div[@class='bx-soa-item-title'])" # [i]
    _item_price_locator = "(//strong[@class='bx-price all'])" # [i]

    _price_for_all_locator = "//*[@id='bx-soa-total']/div[2]/div[1]/span[2]"
    _delivery_price_locator = "//*[@id='bx-soa-total']/div[2]/div[3]/span[2]"
    _total_price_locator = "//*[@id='bx-soa-total']/div[2]/div[5]/span[2]"


    @allure.title("check products' data match")
    def check_products_data_match(self):
        a = 0  # для расчёта стоимости доставки
        sum_price = 0 # сумма всех товаров, которая берётся из айтема и потом суммируется

        get_price_for_all = self.wait_to_be_visible(self._price_for_all_locator).text # цена за всё в правом блоке
        price_for_all = self.divide_price(get_price_for_all)

        get_total_price = self.wait_to_be_visible(self._total_price_locator).text # итоговая цена
        total_price = self.divide_price(get_total_price)

        for i in range(1,count):
            # inner locators
            item_name_locator = f"{self._item_name_locator}[{i}]"
            item_name = self.wait_to_be_visible(item_name_locator).text.lower()

            item_price_locator = f"{self._item_price_locator}[{i}]"
            get_item_price = self.wait_to_be_visible(item_price_locator).text
            item_price = self.divide_price(get_item_price)

            assert Database.select_item_data(i)[1] == item_name
            assert item_price == Database.select_item_data(i)[2] - (Database.select_item_data(i)[2] - item_price)
            sum_price += item_price
        assert round(sum_price,2) == price_for_all
        assert round(sum_price,2) == total_price
