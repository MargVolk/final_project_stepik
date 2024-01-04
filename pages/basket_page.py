from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    _url = "http://selenium1py.pythonanywhere.com/basket/"

    def __init__(self, browser, url=_url):
        super(BasketPage, self).__init__(browser, url)

    def basket_is_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT, "Products in basket")
        assert ("Your basket is empty. Continue shopping" ==
                self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text), "Text empty basket is not present"
