import allure
from helpers.ui_helper import UIHelper

class BasePage(UIHelper):

    search_city_name = "Ижевск"

    # locators

    ## main user links

    _enter_btn_locator = "(//div[@class='header__actions-item'])[1]"
    _favorite_btn_locator = "(//div[@class='header__actions-item'])[2]"
    _cart_btn_locator = "(//div[@class='header__actions-item'])[3]"

    # navbar

    catalogue_button_locator = "(//div[@class='hr3-menu__item__submenu hr3-menu__item-wrap'])[1]"

    ## choose city

    _search_input_locator = "//input[@id='smart-title-search-input']"
    _select_city_popup_locator = "//div[@class='select-city__dropdown']"
    _choose_yes_btn_locator = "//span[@class='btn select-city__dropdown__choose__yes select-city__dropdown__choose']"
    _choose_no_btn_locator = "//span[@class='btn select-city__dropdown__choose__no select-city__dropdown__choose']"
    _select_city_window_locator = "//div[@class='select-city__modal-wrap']"
    _search_city_input_locator = "//input[@class='select-city__input']"
    _select_city_close_popup = "//div[@class='select-city__close']"
    dropdown_city_name_locator = "(//div[@class='select-city__block__text'])[2]"

    ## authorization

    _pop_up_title_locator = "//h3[@class='bx-title']"
    _input_email_locator = "//input[@name='USER_LOGIN']"
    _input_user_password_locator = "//input[@name='USER_PASSWORD']"
    _checkbox_locator = "//label[@class='bx-filter-param-label']"
    _login_button_locator = "//input[@class='btn btn-primary']"

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

    @allure.step("get popup title")
    def get_popup_title(self):
        element = self.wait_to_be_visible(self._pop_up_title_locator)
        assert element.text == "Пожалуйста, авторизуйтесь"

    @allure.step("authorization: enter email")
    def auth_enter_email(self, email):
        self.wait_to_be_clickable(self._input_email_locator).send_keys(email)

    @allure.step("authorization: enter password")
    def auth_enter_password(self, password):
        self.wait_to_be_clickable(self._input_user_password_locator).send_keys(password)

    @allure.step("authorization: click enter button")
    def auth_click_enter_button(self):
        self.wait_to_be_clickable(self._login_button_locator).click()

    @allure.step("Hover catalogue button")
    def hover_catalogue_button(self):
        self.hover(self.catalogue_button_locator)

    @allure.step("hover link in catalogue: 1st lvl")
    def hover_link_in_catalogue_1st_lvl(self, index):
        locator = "//div[@class='catalog-menu__inner']/div"+f"[{index}]/a"
        self.hover(locator)

    @allure.step("hover link in catalogue: 2st lvl")
    def hover_link_in_catalogue_2st_lvl(self, index, click=False):
        locator = "//*[@id='page-wrapper']/div[1]/header/div/div[3]/div/div[1]/div/div/div[4]/div/div/div"+f"[{index}]/div/a"
        if click:
            self.wait_to_be_clickable(locator).click()
        else:
            self.hover(locator)

    # methods

    @allure.step("Choose city from results")
    def choose_city_from_result(self):
        locator = f"//p[contains(text(), ' {self.search_city_name} ')]"
        self.wait_to_be_clickable(locator).click()

    @allure.step("Check city name align")
    def check_city_name_align(self):
        self.driver.refresh()
        locator = self.wait_to_be_visible(self.dropdown_city_name_locator)
        assert self.search_city_name == locator.text