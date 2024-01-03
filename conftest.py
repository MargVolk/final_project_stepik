import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as op_firefox
from selenium.webdriver.chrome.options import Options as op_chrome


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru or en")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome" and user_language in ['ru', 'en']:
        print(f"\nstart {browser_name}browser for test with {user_language}..")
        options = op_chrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox" and user_language in ['ru', 'en']:
        print(f"\nstart {browser_name}browser for test with {user_language}..")
        options = op_firefox()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox, --language should be ru or en")
    yield {'browser': browser, 'language': user_language}
    print("\nquit browser..")
    browser.quit()
