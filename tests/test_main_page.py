from pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        driver = browser.get('browser')
        main_page = MainPage(driver, "http://selenium1py.pythonanywhere.com/")
        main_page.open()
        main_page.go_to_login_page()
