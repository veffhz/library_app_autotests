from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
