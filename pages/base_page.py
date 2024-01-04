import math

from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.__open()

    def __open(self):
        self.browser.get(self.url)

    def go_to_page(self, page_class, element):
        self.browser.find_element(*element).click()
        return page_class(self.browser, self.browser.current_url)

    def should_be_login_button(self):
        self.is_element_present(*BasePageLocators.LOGIN_LINK, "Login link")

    def element_present(self, how, what, timeout=4) -> bool:
            try:
                WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
            except TimeoutException:
                return False
            return True

    def is_element_present(self, how, what, label_element="Element", timeout=4):
        assert self.element_present(how, what, timeout=timeout), f"{label_element} is not present"

    def is_not_element_present(self, how, what, label_element="Element", timeout=4):
        assert not self.element_present(how, what, timeout=timeout), f"{label_element} is present"

    def is_disappeared(self, how, what, label_element="Element", timeout=4):
        def element_disappeared():
            try:
                WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                    EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return False
            return True

        assert element_disappeared(), f"{label_element} hasn't disappeared"

    def should_be_authorized_user(self):
        self.is_element_present(*BasePageLocators.USER_ICON, "User icon")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")