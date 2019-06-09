from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time


USER = "usr"
PASSWORD = "password"
URL = "http://localhost:8080/login"


def main():
    browser = webdriver.Chrome()
    browser.get(URL)

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "form-signin-heading"), "Please sign in")
    )

    login_field = browser.find_element_by_id("username")
    login_field.send_keys(USER)

    password_field = browser.find_element_by_id("password")
    password_field.send_keys(PASSWORD)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)

    info_text_h1 = browser.find_element_by_tag_name("h1")
    h1_text = info_text_h1.text

    assert "Info" == h1_text

    info_text_p = browser.find_element_by_tag_name("p")
    p_text = info_text_p.text

    assert "Now we have:" == p_text


if __name__ == "__main__":
    main()
