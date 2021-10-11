from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.link = "http://suninjuly.github.io/registration2.html"  # подставляем адрес нужной страницы
        self.browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
        self.browser.get(self.link)
        self.time.sleep(3)
        # ищем поля по уникальным селекторам, при этом проверяя их обязательность(наличие тега required)
        self.first_name = self.browser.find_element_by_css_selector('input.first[required]')
        self.first_name.send_keys("Ivan")
        self.last_name = self.browser.find_element_by_css_selector('input.second[required]')
        self.last_name.send_keys("Petrov")
        self.e_mail = self.browser.find_element_by_css_selector("input.third[required]")
        self.e_mail.send_keys("i.p@smolensk.ru")
        # смотрим на результат либо падаем в ошибку NoSuchElementException(ловить не стал, т.к. в задании не просят)
        self.time.sleep(3)
    def test_abs2(self):
        self.browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
        self.button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
        self.button.click()  # нажми на кнопку - получишь результат)))
        self.time.sleep(5)
        self.welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual( self.welcome_text, 'Congratulations! You have successfully registered!')
if __name__ == "__main__":
    unittest.main()