import allure
from pages.base_page.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException

class DeliveryService(BasePage):

    # locators

    origin_locator = "(//div[@class='bx-soa-pp-item-container'])[1]/div"

    _sdek_pickup_locator = origin_locator + "[1]"
    _sdek_courier_locator = origin_locator + "[2]"
    _sdek_postamat_locator = origin_locator + "[3]"
    _post_courier_locator = origin_locator + "[4]"
    _post_pickup_online_locator = origin_locator + "[5]"
    _post_pickup_standart_locator = origin_locator + "[6]"

    # actions

    @allure.step("click SDEK pickup")
    def click_sdek_pickup(self):
        try:
            self.wait_to_be_clickable(self._sdek_pickup_locator).click()
        except StaleElementReferenceException:
            self.wait_to_be_clickable(self._sdek_pickup_locator).click()

    @allure.step("click SDEK courier")
    def click_sdek_courier(self):
        try:
            self.wait_to_be_clickable(self._sdek_courier_locator).click()
        except StaleElementReferenceException:
            self.wait_to_be_clickable(self._sdek_courier_locator).click()

    @allure.step("click SDEK postamat")
    def click_sdek_postamat(self):
        try:
            self.wait_to_be_clickable(self._sdek_postamat_locator).click()
        except StaleElementReferenceException:
            self.wait_to_be_clickable(self._sdek_postamat_locator).click()

    @allure.step("click post courier")
    def click_post_courier(self):
        try:
            self.wait_to_be_clickable(self._post_courier_locator).click()
        except StaleElementReferenceException:
            self.wait_to_be_clickable(self._post_courier_locator).click()

    @allure.step("click post pickup online")
    def click_post_pickup_online(self):
        try:
            self.wait_to_be_clickable(self._post_pickup_online_locator).click()
        except StaleElementReferenceException:
            self.wait_to_be_clickable(self._post_pickup_online_locator).click()

    @allure.step("click post pickup standart")
    def click_post_pickup_standart(self):
        try:
            self.wait_to_be_clickable(self._post_pickup_standart_locator).click()
        except StaleElementReferenceException:
            self.wait_to_be_clickable(self._post_pickup_standart_locator).click()