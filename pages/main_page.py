from pages.base_page import BasePage


class MainPage(BasePage):
    _url = "https://selenium1py.pythonanywhere.com/"

    def __init__(self, browser, url=_url):
        super(MainPage, self).__init__(browser, url)
