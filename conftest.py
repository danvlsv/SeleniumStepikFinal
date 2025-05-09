import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")

    if user_language not in ["es",'fr','en']:
        raise pytest.UsageError("--language should be in ['es','fr','en']")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()