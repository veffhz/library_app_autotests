from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
