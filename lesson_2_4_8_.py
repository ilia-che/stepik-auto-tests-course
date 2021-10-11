from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    # ищем поле цеа и ждем пока она будет = $100
    price = WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    # жмём на кропку book
    book = browser.find_element_by_css_selector('#book').click()
    # ищем х, вычисляем и заполняем ответом поле
    x_field = browser.find_element_by_css_selector('#input_value')
    x = int(x_field.text)
    result = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(result)

    time.sleep(2)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()  # нажми на кнопку - получишь результат)))
    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()