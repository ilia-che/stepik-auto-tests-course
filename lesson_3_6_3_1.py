import pytest
import time
import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_math_alien(link):
    try:
        print("\nstart browser for test..")
        browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
        browser.implicitly_wait(25)
        browser.get(f'https://stepik.org/lesson/{link}/step/1')
        number = math.log(int(time.time()))
        print('number: '+str(number))
        answer = browser.find_element_by_css_selector("div textarea")
        answer.click()
        print('found..')
        answer.send_keys(str(number))
        print('sent..')
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        print('found..')
        button.click()
        print('click..')
        print('answer sent..')
        congratulation = browser.find_element_by_css_selector('.smart-hints__hint')
        print('congratilatio text:', congratulation.text)
        assert congratulation.text == 'Correct!', 'Answer is not Correct!'
    finally:
        print("\nquit browser..")
        browser.quit()