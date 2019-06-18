import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_test import BaseTest
from .config import TITLE_CORRECT, ADMIN_ROLE, ADMIN_PASSWORD


class TestPageAuthor(BaseTest):
    @pytest.mark.regression
    def test_author_page_usr(self, browser):
        wait = WebDriverWait(browser, 5)

        self.login(browser, wait)

        wait.until(EC.title_is(TITLE_CORRECT))

        author_button = browser.find_element_by_xpath("//li[@class='nav-item']/a[text()='Author']")
        author_button.click()

        info_text_h1 = browser.find_element_by_tag_name("h1")
        h1_text = info_text_h1.text

        h1_text_correct = "Authors:"

        assert h1_text_correct == h1_text, \
            f"Should be '{h1_text_correct}', but got '{h1_text}'"

        self._create_author(browser)

        self._delete_author(browser, "Error")

        self.logout(browser, wait)

    @pytest.mark.regression
    def test_author_page_adm(self, browser):
        wait = WebDriverWait(browser, 5)

        self.login(browser, wait, user=ADMIN_ROLE, password=ADMIN_PASSWORD)

        wait.until(EC.title_is(TITLE_CORRECT))

        author_button = browser.find_element_by_xpath("//li[@class='nav-item']/a[text()='Author']")
        author_button.click()

        info_text_h1 = browser.find_element_by_tag_name("h1")
        h1_text = info_text_h1.text

        h1_text_correct = "Authors:"

        assert h1_text_correct == h1_text, \
            f"Should be '{h1_text_correct}', but got '{h1_text}'"

        self._create_author(browser)

        self._delete_author(browser, "Success")

        self.logout(browser, wait)

    def _create_author(self, browser):
        input_first_name = browser.find_element_by_css_selector("form input[placeholder='First Name']")
        input_first_name.send_keys("Sergei")

        input_date = browser.find_element_by_css_selector("form input[type='date']")
        input_date.send_keys("04/11/1968")

        input_last_name = browser.find_element_by_css_selector("form input[placeholder='Last Name']")
        input_last_name.send_keys("Lukyanenko")

        save_button = browser.find_element_by_css_selector("form input[type='submit']")
        save_button.click()

        WebDriverWait(browser, 3).until(
            EC.visibility_of_element_located((By.ID, "authorSuccess"))
        )

        WebDriverWait(browser, 3).until(
            EC.invisibility_of_element_located((By.ID, "authorSuccess"))
        )

    def _delete_author(self, browser, result):
        table = browser.find_element(By.CLASS_NAME, 'items')
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in reversed(rows):
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) > 1 and cols[1].text == "Sergei Lukyanenko":
                del_button = cols[2].find_element_by_css_selector("input[value='x']")
                del_button.click()

                WebDriverWait(browser, len(rows) * 2).until(  # TODO doc
                    EC.visibility_of_element_located((By.ID, f"author{result}"))
                )

                WebDriverWait(browser, len(rows) * 2).until(  # TODO doc
                    EC.invisibility_of_element_located((By.ID, f"author{result}"))
                )
