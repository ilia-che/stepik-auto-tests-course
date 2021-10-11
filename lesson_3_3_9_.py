import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
'''
def test_exception1():
    try:
        browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()'''

from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_css_selector(".first_block .first").send_keys("Тест")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Остерон")
        browser.find_element_by_css_selector(".first_block .third").send_keys("t100steron@test.ru")

        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_registration2(self):
        browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_css_selector(".first_block .first").send_keys("Тест")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Остерон")
        browser.find_element_by_css_selector(".first_block .third").send_keys("t100steron@test.ru")

        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()