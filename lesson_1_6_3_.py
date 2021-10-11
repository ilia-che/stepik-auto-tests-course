from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)
    button = browser.find_element(By.ID,"submit_button")
    #print('@@@@', type(button),type(browser), browser, button, sep='@@@\n@@@')
    button.click()
    time.sleep(15)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
