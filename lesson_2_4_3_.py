from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get("http://suninjuly.github.io/wait2.html")
    browser.implicitly_wait(5)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()