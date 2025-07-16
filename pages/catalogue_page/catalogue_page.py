import allure
from pages.base_page.base_page import BasePage
from pages.catalogue_page.components.filters import Filters
from count import count

class CataloguePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = Filters(driver)

        # locators

        ## item components

        item_favourite_btn_locator = "(//div[@class='product-item__favorite favorite-icon h2o_add_favor'])"
        item_brand_locator = "(//div[@class='product-item__title-brand'])"
        item_name_locator = "(//div[@class='product-item__title-name'])"
        item_price_locator = "(//div[@class='product-item__price-current'])"
        item_add_to_cart_btn_locator = "(//div[@class='product-item__cart'])"

        ## popup components

        popup_brand_locator = "//div[@class='like_h1']" # .text
        popup_name_locator = "//h2[@class='like_h2']"
        popup_price_locator = "//div[@class='ctp_current']" # .text
        popup_go_to_cart_btn_locator = "//a[@id='link']"
        keep_shopping_btn_locator = "(//a[@class='d_close btn'])[1]"
