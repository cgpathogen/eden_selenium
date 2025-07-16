import allure
from pages.base_page.base_page import BasePage

class Filters(BasePage):

    # locators

    ## dropdown 1

    _select_sort_options_dropdown_locator = "//div[@class='jq-selectbox jqselect catalog-content__sort__type-select styler']"
    _option_sel_by_new_locator = "//option[contains(text(),'По новизне')]"
    _option_sel_by_price_asc = "//option[contains(text(),'По возрастанию цены')]"
    _option_sel_by_price_desc = "//option[contains(text(),'По возрастанию цены')]"

    ## dropdown 2

    _select_by_amount_locator = "//div[@class='jq-selectbox jqselect catalog-content__sort__type-select elements-on styler changed']"
    _select_by_twelve_locator = "//option[contains(text(),'12')]"
    _select_by_twenty_four_locator = "//option[contains(text(),'24')]"
    _select_by_thirty_six_locator = "//option[contains(text(),'36')]"
    _select_by_forty_eight_locator = "//option[contains(text(),'48')]"

    ## price locators

    _min_price_input_locator = "//input[@id='scentFilter_381_MIN']"
    _max_price_input_locator = "//input[@id='scentFilter_381_MAX']"
    _show_results_by_price_btn_locator = "//div[@id='modef']"
    _left_range_slider_locator = "//div[@class='noUi-handle noUi-handle-lower']"
    _right_range_slider_locator = "//div[@class='noUi-handle noUi-handle-upper']"

    # actions_

    ## ============================= OPTIONS DROPDOWN

    @allure.step("Click sort options dropdown")
    def click_sort_options_dropdown(self):
        self.wait_to_be_clickable(self._select_sort_options_dropdown_locator).click()

    @allure.step("Click sort by new")
    def click_sort_by_new(self):
        self.wait_to_be_clickable(self._option_sel_by_new_locator).click()

    @allure.step("Click sort by price (asc)")
    def click_sort_by_price_asc(self):
        self.wait_to_be_clickable(self._option_sel_by_price_asc).click()

    @allure.step("Click sort by price (desc)")
    def click_sort_by_price_desc(self):
        self.wait_to_be_clickable(self._option_sel_by_price_desc).click()

    ## ============================= BY AMOUNT DROPDOWN DROPDOWN

    @allure.step("Click select by amount locator")
    def click_select_by_amount_dropdown(self):
        self.wait_to_be_clickable(self._select_by_amount_locator).click()

    @allure.step("Select by twelve")
    def click_select_by_twelve(self):
        self.wait_to_be_clickable(self._select_by_twelve_locator).click()

    @allure.step("Select by twenty four")
    def click_select_by_twenty_four_locator(self):
        self.wait_to_be_clickable(self._select_by_twenty_four_locator).click()

    @allure.step("Select by thirty six four")
    def click_select_by_thirty_six(self):
        self.wait_to_be_clickable(self._select_by_thirty_six_locator).click()

    @allure.step("Select by forty eight")
    def click_select_by_forty_eight(self):
        self.wait_to_be_clickable(self._select_by_forty_eight_locator).click()

    # PRICE SORT

    @allure.step("enter min price")
    def enter_min_price(self, price):
        element = self.wait_to_be_clickable(self._min_price_input_locator)
        element.send_keys(price)


    @allure.step("enter max price")
    def enter_max_price(self, price):
        element = self.wait_to_be_clickable(self._max_price_input_locator)
        element.send_keys(price)


    @allure.step("drag min price slider")
    def drag_min_price_locator(self, num):
        element = self.wait_to_be_clickable(self._left_range_slider_locator)
        self.actions.move_to_element(element).click_and_hold(element).move_by_offset(num, 0).release().perform()


    @allure.step("drag max price slider")
    def drag_max_price_locator(self, num):
        element = self.wait_to_be_clickable(self._right_range_slider_locator)
        self.actions.move_to_element(element).click_and_hold(element).move_by_offset(num, 0).release().perform()

    @allure.step("Click show results by price button")
    def click_show_results_by_price_btn(self):
        element = self.wait_to_be_clickable(self._show_results_by_price_btn_locator)
        element.click()