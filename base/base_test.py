from pages.main_page.main_page import MainPage

from data.credentials.credentials import Credentials

class BaseTest:

    def setup_method(self):
        self.mainPage = MainPage(self.driver)
        self.credentials = Credentials()