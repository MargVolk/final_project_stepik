from faker import Faker

from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators
from pages.main_page import MainPage


class LoginPage(BasePage):
    _url = "https://selenium1py.pythonanywhere.com/accounts/login/"

    def __init__(self, browser, url=_url):
        super(LoginPage, self).__init__(browser, url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Text 'login' should be present in current url"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM, "Login Form")

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTRATION_FROM, "Registration form")

    def register_new_user(self):
        fake = Faker()
        password = fake.password()

        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fake.email())
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

        self.should_be_authorized_user()

    def check_elements_for_main_page_after_registration(self):
        assert MainPage._url == self.browser.current_url[:-6], "Not redirect to Main Page"
        assert "Thanks for registering!" == self.browser.find_element(*MainPageLocators.ALERT_SUCCESS_REGISTER).text, \
            "Registration is not success"
