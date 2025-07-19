import allure

from database.database import Database
from pages.base_page.base_page import BasePage
from pages.catalogue_page.components.filters import Filters
from count import count

class CataloguePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = Filters(driver)

    # locators

    _item_locator = "//div[@class='product-list-item']"

    ## item components

    _item_favourite_btn_locator = "//div[@class='product-item__favorite favorite-icon h2o_add_favor']"
    _item_brand_locator = "(//div[@class='product-item__title-brand'])"
    _item_name_locator = "(//div[@class='product-item__title-name'])"
    _item_price_locator = "(//div[@class='product-item__price-current'])"
    _item_add_to_cart_btn_locator = "(//div[contains(@class, 'product-item__cart-btn')])"

    ## popup components

    _popup_locator = "//div[@class='dialog d_small cart-popup']"
    _popup_brand_locator = "//div[@class='like_h1']" # .text
    _popup_name_locator = "//h2[@class='like_h2']"
    _popup_price_locator = "//div[@class='ctp_current']" # .text
    _popup_go_to_cart_btn_locator = "//a[@id='link']"
    _keep_shopping_btn_locator = "(//a[@class='d_close btn'])[1]"

    # methods

    @allure.step("Add goods to cart")
    def add_goods_to_cart(self):
        for i in range(1, count):
            # inner locators
            item_locator = f"{self._item_locator}[{i}]"

            item_brand_locator = f"{self._item_brand_locator}[{i}]"
            item_brand = self.wait_to_be_visible(item_brand_locator).text.lower()

            item_name_locator = f"{self._item_name_locator}[{i}]"
            item_name = self.wait_to_be_visible(item_name_locator).text.lower()

            item_price_locator = f"{self._item_price_locator}[{i}]"
            item_price = self.divide_price(self.wait_to_be_visible(item_price_locator).text)

            add_to_cart_button = f"{self._item_add_to_cart_btn_locator}[{i}]"

            # main algorythm
            self.hover(item_locator) # ховер на карточку товара
            Database.update_data(item_brand, item_name, item_price) # cохранение бренда имени и цены в базу данных
            self.wait_to_be_clickable(add_to_cart_button).click() # клик на кнопку добавления товара
            self.hover(self._popup_locator) # ожидание поп-апа

            # popup locators
            ## парсинг данных из поп-апа

            popup_brand = self.wait_to_be_visible(self._popup_brand_locator).text.lower()
            popup_item_name = self.wait_to_be_visible(self._popup_name_locator).text.lower()
            get_popup_item_price = self.wait_to_be_visible(self._popup_price_locator).text # удаление знака рубля от цены
            popup_item_price = self.divide_price(get_popup_item_price) # цена

            assert Database.select_item_data(i)[0] == popup_brand
            assert Database.select_item_data(i)[1] == popup_item_name
            assert Database.select_item_data(i)[2] == popup_item_price

            self.wait_to_be_clickable(self._keep_shopping_btn_locator).click() # клик "продолжить покупку"

    @allure.step("Parse items data")
    def parse_items_data(self):
        """
        метод проверяет наличие текста из популярного запроса в названии элемента в каталоге
        """
        for i in range(2,5+1):
            self.hover(self._search_field_locator)
            request_locator = f"{self._popular_request_locator}[{i}]"
            request_text = self.wait_to_be_visible(request_locator).text.lower()
            self.wait_to_be_clickable(request_locator).click()

            elements = self.find_several_elements(self._item_name_locator)
            for element in elements:
                assert request_text in element.text.lower()

            self.clear_field(self._search_field_locator)