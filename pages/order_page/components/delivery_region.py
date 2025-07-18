import allure
from pages.base_page.base_page import BasePage

class DeliveryRegion(BasePage):

    # locators

    _input_locator = "(//input[@class='bx-ui-sls-fake'])[1]"
    _tooltip_locator = "(//div[@class='tooltip-inner'])[1]"

    # actions

    @allure.step("Enter delivery region")
    def enter_delivery_region(self, region):
        self.wait_to_be_clickable(self._input_locator).send_keys(region)

    @allure.step("get tooltip text")
    def get_region_tooltip_text(self):
        element = self.wait_to_be_visible(self._tooltip_locator)
        return element.text.lower()