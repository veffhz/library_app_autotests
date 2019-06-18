from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .config import URL, USER, USER_PASSWORD


class BaseTest:
    @staticmethod
    def login(browser, wait):
        browser.get(URL)
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "form-signin-heading"), "Please sign in")
        )

        login_field = browser.find_element_by_id("username")
        login_field.send_keys(USER)

        password_field = browser.find_element_by_id("password")
        password_field.send_keys(USER_PASSWORD)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    @staticmethod
    def logout(browser, wait):
        button = browser.find_element_by_css_selector(".button-cosmo")
        button.click()

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".alert-success"), "You have been signed out")
        )
