import pytest

from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators, BasePageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/?promo=newYear2019")
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_alert_success_after_add()
        product_page.check_alert_success_after_add()
        product_page.check_total_basket_after_add()

    @pytest.mark.skip
    @pytest.mark.parametrize('promo_value', [no for no in range(10)])
    def test_promo_offer(self, browser, promo_value):
        product_page = ProductPage(browser, f"coders-at-work_207/?promo=offer{promo_value}")
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_alert_success_after_add()
        product_page.check_alert_success_after_add()
        product_page.check_total_basket_after_add()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/")
        product_page.add_product_to_basket()
        product_page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT, "Success message")

    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/")
        product_page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT, "Success message")

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/")
        product_page.add_product_to_basket()
        product_page.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT, "Success message")

    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductPage(browser, "the-city-and-the-stars_95/")
        product_page.should_be_login_button()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_page = ProductPage(browser, "the-city-and-the-stars_95/")
        product_page.go_to_page(LoginPage, BasePageLocators.LOGIN_LINK)

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/")
        basket_page = product_page.go_to_page(BasketPage, BasePageLocators.BASKET_LINK)
        basket_page.basket_is_empty()


@pytest.mark.userProducts
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.register_new_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/")
        product_page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT, "Success message")

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, "coders-at-work_207/?promo=newYear2019")
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_alert_success_after_add()
        product_page.check_alert_success_after_add()
        product_page.check_total_basket_after_add()
