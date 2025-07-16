from pages.main_page.main_page import MainPage
from pages.personal_cabinet_page.personal_cabinet_page import PersonalCabinetPage
from pages.catalogue_page.catalogue_page import CataloguePage

from data.credentials.credentials import Credentials

class BaseTest:

    def setup_method(self):
        self.mainPage = MainPage(self.driver)
        self.personalCabinetPage = PersonalCabinetPage(self.driver)
        self.cataloguePage = CataloguePage(self.driver)
        self.credentials = Credentials()