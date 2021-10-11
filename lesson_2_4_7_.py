from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.common import exceptions as ex

try:
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

    time.sleep(15)
except ex.NoSuchElementException: print('No Such Element Exception!')
except ex.TimeoutException: print('Timeout Exception!')
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()