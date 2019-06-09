from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

USER_ROLE = "usr"
ADMIN_ROLE = "adm"
PASSWORD = "password"
URL = "http://localhost:8080/login"

browser = webdriver.Chrome()
browser.get(URL)
browser.implicitly_wait(5)


def login():
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "form-signin-heading"), "Please sign in")
    )

    login_field = browser.find_element_by_id("username")
    login_field.send_keys(ADMIN_ROLE)

    password_field = browser.find_element_by_id("password")
    password_field.send_keys(PASSWORD)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def create():
    input_first_name = browser.find_element_by_css_selector("form input[placeholder='First Name']")
    input_first_name.send_keys("Sergei")

    input_date = browser.find_element_by_css_selector("form input[type='date']")
    input_date.send_keys("04/11/1968")

    input_last_name = browser.find_element_by_css_selector("form input[placeholder='Last Name']")
    input_last_name.send_keys("Lukyanenko")

    save_button = browser.find_element_by_css_selector("form input[type='submit']")
    save_button.click()

    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.ID, 'authorSuccess'))
    )


def delete():
    table = browser.find_element(By.CLASS_NAME, 'items')
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in reversed(rows):
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) > 1 and cols[1].text == "Sergei Lukyanenko":
            del_button = cols[2].find_element_by_css_selector("input[value='x']")
            del_button.click()

            WebDriverWait(browser, 3).until(
                EC.visibility_of_element_located((By.ID, 'authorSuccess'))
            )


def main():
    login()

    author_button = browser.find_element_by_xpath("//li[@class='nav-item']/a[text()='Author']")
    author_button.click()

    info_text_h1 = browser.find_element_by_tag_name("h1")
    h1_text = info_text_h1.text

    assert "Authors:" == h1_text

    create()

    delete()


if __name__ == "__main__":
    main()
