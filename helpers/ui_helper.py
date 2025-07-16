import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UIHelper:

    def __init__(self, driver):
        self.driver : WebDriver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(driver,timeout=10,poll_frequency=1)

    # open

    @allure.step("Open page")
    def open(self):
        with allure.step(f"Open page {self.page_url}"):
            self.driver.get(self.page_url)

    # waits

    def wait_to_be_clickable(self, locator, index=None):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.locator_maker(locator,index)))
        except StaleElementReferenceException:
            element = self.wait.until(EC.element_to_be_clickable(self.locator_maker(locator,index)))
        return element

    def wait_to_be_visible(self, locator, index=None):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.locator_maker(locator, index)))
        except StaleElementReferenceException:
            element = self.wait.until(EC.visibility_of_element_located(self.locator_maker(locator, index)))
        return element

    # actions

    def hover(self, locator, index=None):
        element = self.wait_to_be_visible(locator, index)
        self.actions.move_to_element(element).perform()

    # scrolls

    @allure.step("scrolling page")
    def scroll(self,up, down):
        self.driver.execute_script(f"window.scrollBy({up}, {down});")

    # other

    def locator_maker(self, xpath, index=None, option=None):
        """
        универсальный метод во избежание дублирования кода
        """
        if index is not None:
            return ("xpath",f"{xpath}[{index}]")
        if option is not None:
            return ("xpath", f"{xpath}[{index}]{option}")
        return ("xpath", xpath)