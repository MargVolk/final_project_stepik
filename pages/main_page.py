from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):

    __url = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser):
        super().__init__(browser, MainPage.__url)

    def go_to_login_page(self) -> LoginPage:
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return self.create_page(LoginPage)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


