from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    #time.sleep(1)
    # ищем х, вычисляем и заполняем ответом поле
    num1 = browser.find_element_by_css_selector('#num1')
    num2 = browser.find_element_by_css_selector('#num2')
    result = str(int(num1.text)+int(num2.text))
    print(result)
    answer = Select(browser.find_element_by_css_selector('#dropdown'))
    answer.select_by_visible_text(result)
    # прожимаем чекбокс и радиобатн

    time.sleep(2)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()  # нажми на кнопку - получишь результат)))
    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()