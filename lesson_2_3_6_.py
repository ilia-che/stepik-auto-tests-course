from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(3)
    windows = browser.window_handles
    print(windows)
    switch_window = browser.switch_to.window(windows[1])
    # ищем х, вычисляем и заполняем ответом поле
    x_field = browser.find_element_by_css_selector('#input_value')
    x = int(x_field.text)
    result = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(result)
    time.sleep(1)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()  # нажми на кнопку - получишь результат)))
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
    time.sleep(2)
    alert.dismiss()
    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()