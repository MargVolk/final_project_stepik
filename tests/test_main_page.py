from pages.basket_page import BasketPage
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_page(LoginPage, BasePageLocators.LOGIN_LINK)

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser)
        main_page.should_be_login_button()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser)
        basket_page = main_page.go_to_page(BasketPage, BasePageLocators.BASKET_LINK)
        basket_page.basket_is_empty()
