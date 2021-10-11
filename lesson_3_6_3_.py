import pytest
import time
import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895"])#, "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_math_alien(browser, link):
    browser.get(f'https://stepik.org/lesson/{link}/step/1')
    number = math.log(int(time.time()))
    print('number: '+str(number))
    print('get..')
    time.sleep(10)
    answer = browser.find_element_by_css_selector('#ember85')
    print('found..')
    time.sleep(3)
    answer.send_keys(number)
    print('sent..')
    time.sleep(3)
    button = browser.find_element_by_css_selector('.submit-submission')
    print('found..')
    time.sleep(3)
    button.click()
    print('click..')
    print('answer sent..')
    time.sleep(3)
    congratulation = browser.find_element_by_css_selector('.smart-hints__hint')
    print('congratilatio text:', congratulation.text)
    assert congratulation.text == 'Correct!'