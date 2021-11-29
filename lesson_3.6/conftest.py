import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                    help="Choose language: ru, en, ...")                


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    