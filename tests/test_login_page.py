from pages.login_page import LoginPage


class TestRegistration:
    def test_registration_user(self, browser):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
        login_page.register_new_user()
        login_page.check_elements_for_main_page_after_registration()
