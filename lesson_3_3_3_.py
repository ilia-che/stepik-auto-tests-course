from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def reg(link):

    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    input3.send_keys("test@test.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    return browser.find_element_by_tag_name("h1").text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


class TestAll(unittest.TestCase):
    def test_first_link(self):
        self.assertEquals(reg(link1), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')

    def test_first_link2(self):
        self.assertEquals(reg(link2), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')

if __name__ == "__main__":
        unittest.main()