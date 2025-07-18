from pages.main_page.main_page import MainPage
from pages.personal_cabinet_page.personal_cabinet_page import PersonalCabinetPage
from pages.catalogue_page.catalogue_page import CataloguePage
from pages.cart_page.cart_page import CartPage
from pages.order_page.order_page import OrderPage

from data.credentials.credentials import Credentials

class BaseTest:

    def setup_method(self):
        self.mainPage = MainPage(self.driver)
        self.personalCabinetPage = PersonalCabinetPage(self.driver)
        self.cataloguePage = CataloguePage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.orderPage = OrderPage(self.driver)
        self.credentials = Credentials()