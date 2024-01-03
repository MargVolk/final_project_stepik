from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=3) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
            self.browser.find_element(how, what)
        except TimeoutException:
            return False
        return True

    def create_page(self, page_class):
        return page_class(self.browser, self.browser.current_url)
