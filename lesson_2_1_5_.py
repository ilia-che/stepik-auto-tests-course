from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/math.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    time.sleep(1)
    # ищем х, вычисляем и заполняем ответом поле
    x_field = browser.find_element_by_css_selector('#input_value')
    x = int(x_field.text)
    result = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(result)
    # прожимаем чекбокс и радиобатн
    check_box = browser.find_element_by_css_selector('#robotCheckbox').click()
    radio_button = browser.find_element_by_css_selector('#robotsRule').click()

    time.sleep(3)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()  # нажми на кнопку - получишь результат)))
    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()