import allure
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:

    def __init__(self, driver):
        self.driver : WebDriver = driver


    @allure.step("Open page")
    def open(self):
        with allure.step(f"Open page {self.page_url}"):
            self.driver.get(self.page_url)