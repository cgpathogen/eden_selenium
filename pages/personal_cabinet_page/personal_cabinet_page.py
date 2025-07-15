import allure
from pages.base_page.base_page import BasePage
from pages.personal_cabinet_page.components.navigation_links import NavigationLinks

class PersonalCabinetPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.nav_links = NavigationLinks(driver)

    # locators

    _username_locator = "//div[@class='cabinet-info__text cabinet-mail']"

    # actions

    @allure.step("get username")
    def get_username_text(self):
        element = self.wait_to_be_visible(self._username_locator)
        return element.text