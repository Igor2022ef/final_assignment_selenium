import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=es' or '--language=ru' or '--language=fr'")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe', options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxProfile()
        options.set_preference("intl.accept_languages", user_language)
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()








