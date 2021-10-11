from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/cats.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element_by_id("button")
    button.click()

    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()