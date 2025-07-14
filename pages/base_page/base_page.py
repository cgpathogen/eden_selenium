import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver : WebDriver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(driver,timeout=10,poll_frequency=1)


    # locators

    _enter_btn_locator = "//a[@title='Войти']"
    _favorite_btn_locator = "//a[@class='favor-list-wrap icon']"
    _cart_btn_locator = "//a[@title='Корзина']"
    _search_input_locator = "//input[@id='smart-title-search-input']"
    _select_city_popup_locator = "//div[@class='select-city__dropdown']"
    _choose_yes_btn_locator = "//span[@class='btn select-city__dropdown__choose__yes select-city__dropdown__choose']"
    _choose_no_btn_locator = "//span[@class='btn select-city__dropdown__choose__no select-city__dropdown__choose']"
    _select_city_window_locator = "//div[@class='select-city__modal-wrap']"
    _select_city_input_locator = "//input[@class='select-city__input']"
    _select_city_close_popur = "//div[@class='select-city__close']"


    @allure.step("Open page")
    def open(self):
        with allure.step(f"Open page {self.page_url}"):
            self.driver.get(self.page_url)