from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from .config import URL, TITLE_CORRECT
from .config import USER, USER_PASSWORD


@pytest.mark.smoke
def test_info_page(browser):
    browser.get(URL)
    wait = WebDriverWait(browser, 5)

    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "form-signin-heading"), "Please sign in")
    )

    login_field = browser.find_element_by_id("username")
    login_field.send_keys(USER)

    password_field = browser.find_element_by_id("password")
    password_field.send_keys(USER_PASSWORD)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    wait.until(EC.title_is(TITLE_CORRECT))

    h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    p = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))

    h1_text_correct = "Info"

    assert h1_text_correct == h1.text, \
        f"Should be '{h1_text_correct}', but got '{h1.text}'"

    p_text_correct = "Now we have:"

    assert p_text_correct == p.text, \
        f"Should be '{p_text_correct}', but got '{p.text}'"
