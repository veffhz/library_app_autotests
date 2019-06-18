from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from .base_test import BaseTest
from .config import TITLE_CORRECT


class TestPageInfo(BaseTest):
    @pytest.mark.smoke
    def test_info_page(self, browser):
        wait = WebDriverWait(browser, 5)

        self.login(browser, wait)

        wait.until(EC.title_is(TITLE_CORRECT))

        h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        p = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))

        h1_text_correct = "Info"

        assert h1_text_correct == h1.text, \
            f"Should be '{h1_text_correct}', but got '{h1.text}'"

        p_text_correct = "Now we have:"

        assert p_text_correct == p.text, \
            f"Should be '{p_text_correct}', but got '{p.text}'"

        self.logout(browser, wait)
