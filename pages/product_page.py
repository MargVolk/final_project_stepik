import re

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    _url = "https://selenium1py.pythonanywhere.com/catalogue/"

    def __init__(self, browser, parameters=""):
        super(ProductPage, self).__init__(browser, ProductPage._url + parameters)
        self.__total_basket = float(re.split('[£\n]', self.browser.find_element(
            *ProductPageLocators.BASKET_MINI_TOTAL).text)[1])
        self.__name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        self.__price = float(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text[1:])


    def add_product_to_basket(self):
        self.is_element_present(*ProductPageLocators.ADD_BUTTON, "Add button")

        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_be_alert_success_add(self):
        self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT, "Alert success ass product")

    def should_be_alert_info_about_total(self):
       self.is_element_present(*ProductPageLocators.ALERT_INFO_BASKET_TOTAL, "Alert info total basket")

    def check_total_basket_after_add(self):
        self.should_be_alert_info_about_total()

        assert (f"Your basket total is now £{self.__total_basket + self.__price}"
                == self.browser.find_element(*ProductPageLocators.ALERT_INFO_BASKET_TOTAL).text), \
            "Total basket is incorrect in info message"
        self.__total_basket = self.__total_basket + self.__price
        assert (str(self.__total_basket)
                == re.split('[£\n]', self.browser.find_element(*ProductPageLocators.BASKET_MINI_TOTAL).text)[1]), \
            "Total basket is incorrect in mini basket"

    def check_alert_success_after_add(self):
        self.should_be_alert_success_add()

        assert (f"{self.__name} has been added to your basket."
                == self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT).text), \
            "Name product is incorrect in success alert"
