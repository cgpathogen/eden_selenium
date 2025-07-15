import allure

from pages.base_page.base_page import BasePage

class NavigationLinks(BasePage):

    # locators

    origin_locator = "//ul[@class='lk__wrap__menu-wrap']/li"

    _my_cabinet_link_locator = origin_locator+"[1]"
    _current_orders_link_locator = origin_locator+"[2]"
    _personal_data_link_locator = origin_locator+"[3]"
    _change_password_link_locator = origin_locator+"[4]"
    _orders_history_link_locator = origin_locator+"[5]"
    _cart_link_locator = origin_locator+"[6]"
    _favorites_link_locator = origin_locator+"[7]"
    _logout_link_locator = origin_locator+"[8]"

    # actions

    @allure.step("click my cabinet link")
    def click_my_cabinet_link(self):
        self.wait_to_be_clickable(self._my_cabinet_link_locator).click()

    @allure.step("click current orders link")
    def click_current_orders_link(self):
        self.wait_to_be_clickable(self._current_orders_link_locator).click()

    @allure.step("click personal data link")
    def click_personal_data_link(self):
        self.wait_to_be_clickable(self._personal_data_link_locator).click()

    @allure.step("click change password link")
    def click_change_password_link(self):
        self.wait_to_be_clickable(self._change_password_link_locator).click()

    @allure.step("click orders history link")
    def click_orders_history_link(self):
        self.wait_to_be_clickable(self._orders_history_link_locator).click()

    @allure.step("click cart link")
    def click_cart_link(self):
        self.wait_to_be_clickable(self._cart_link_locator).click()

    @allure.step("click favorites link")
    def click_favorites_button(self):
        self.wait_to_be_clickable(self._favorites_link_locator).click()

    @allure.step("click logout link")
    def click_logout_link(self):
        self.wait_to_be_clickable(self._logout_link_locator).click()