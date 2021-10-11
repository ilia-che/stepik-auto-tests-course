from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/huge_form.html"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)
    time.sleep(5)
    field_list = browser.find_elements_by_css_selector('[type="text"]')
    for field in field_list:
        field.send_keys("Lol Kek")
    button2 = browser.find_element(By.CLASS_NAME,"btn-default")
    #print('@@@@', type(button),type(browser), browser, button, sep='@@@\n@@@')
    button2.click()
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
