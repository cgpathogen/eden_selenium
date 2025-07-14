import allure
from base.base_test import BaseTest

@allure.epic("User")
@allure.story("Authorization")
class TestAuthorization(BaseTest):

    def test_authorization_as_registered_user(self):
        self.mainPage.open()