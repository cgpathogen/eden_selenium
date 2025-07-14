import allure

from helpers.ui_helper import UIHelper

class BasePage(UIHelper):

    search_city_name = "Ижевск"

    # locators

    _enter_btn_locator = "//a[@title='Войти']"
    _favorite_btn_locator = "//a[@class='favor-list-wrap icon']"
    _cart_btn_locator = "//a[@title='Корзина']"
    _search_input_locator = "//input[@id='smart-title-search-input']"
    _select_city_popup_locator = "//div[@class='select-city__dropdown']"
    _choose_yes_btn_locator = "//span[@class='btn select-city__dropdown__choose__yes select-city__dropdown__choose']"
    _choose_no_btn_locator = "//span[@class='btn select-city__dropdown__choose__no select-city__dropdown__choose']"
    _select_city_window_locator = "//div[@class='select-city__modal-wrap']"
    _search_city_input_locator = "//input[@class='select-city__input']"
    _select_city_close_popup = "//div[@class='select-city__close']"


    # actions

    @allure.step("click enter to personal cabinet button")
    def click_enter_button(self):
        self.wait_to_be_clickable(self._enter_btn_locator).click()

    @allure.step("click favourite button")
    def click_favorite_button(self):
        self.wait_to_be_clickable(self._favorite_btn_locator).click()

    @allure.step("click cart button")
    def click_cart_button(self):
        self.wait_to_be_clickable(self._cart_btn_locator).click()

    @allure.step("Enter text to search input")
    def enter_text_to_search_input(self, text):
        self.wait_to_be_clickable(self._search_input_locator).send_keys(text)

    @allure.step("click choose yes button")
    def click_choose_yes_button(self):
        self.wait_to_be_clickable(self._choose_yes_btn_locator).click()

    @allure.step("click choose no button")
    def click_choose_no_button(self):
        self.wait_to_be_clickable(self._choose_no_btn_locator).click()

    @allure.step("enter text to search city input")
    def enter_text_to_search_city_input(self, text):
        self.wait_to_be_clickable(self._search_city_input_locator).send_keys(text)

    @allure.step("click close search city popup")
    def click_select_city_close_popup(self):
        self.wait_to_be_clickable(self._select_city_close_popup).click()

    # methods

    @allure.step("Choose city from results")
    def choose_city_from_result(self):
        locator = f"//p[contains(text(), ' {self.search_city_name} ')]"
        self.wait_to_be_clickable(locator).click()