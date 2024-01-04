from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]/span[@class = 'btn-group']/a[contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    ALERT_SUCCESS_REGISTER = (By.XPATH, "//div[contains(@class, 'alert-success')]/div[contains(@class, 'alertinner')]")

class BasketPageLocators:
    BASKET_EMPTY = (By.XPATH, "//div[@class = 'content']//p")
    BASKET_PRODUCT = (By.XPATH, "//div[@class ='basket-items']")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FROM = (By.XPATH, "//form[@id='register_form']")
    EMAIL_INPUT = (By.XPATH, REGISTRATION_FROM[1] + "//input[@name='registration-email']")
    PASSWORD_INPUT = (By.XPATH, REGISTRATION_FROM[1] + "//input[@name='registration-password1']")
    PASSWORD2_INPUT = (By.XPATH, REGISTRATION_FROM[1] + "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, REGISTRATION_FROM[1] + "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'add-to-basket')]")
    BASKET_MINI_TOTAL = (By.XPATH, "//div[contains(@class, 'basket-mini')]")
    NAME_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRICE_PRODUCT = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class,'price')]")
    ALERT_SUCCESS_ADD_PRODUCT = (By.XPATH, "(//div[contains(@class, 'alert-success')]/div[@class='alertinner '])[1]")
    ALERT_INFO_BASKET_TOTAL = (By.XPATH, "//div[contains(@class, 'alert-info')]/div[@class='alertinner ']/p[1]")