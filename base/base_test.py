from pages.main_page.main_page import MainPage

class BaseTest:

    def setup_method(self):
        self.mainPage = MainPage(self.driver)