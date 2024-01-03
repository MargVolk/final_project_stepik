from pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()

    def test_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page().should_be_login_page()
