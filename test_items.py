import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_is_button_visible(browser):
    time.sleep(30)
    browser.get(link)
    element = WebDriverWait(browser, 15).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[type="submit"]')))


    assert len(element) > 0