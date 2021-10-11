from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)

    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys("Petrov")
    e_mail = browser.find_element_by_css_selector('[name="email"]')
    e_mail.send_keys("i.p@smolensk.ru")
    dir_name = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_name, 'text.txt')
    upload_file = browser.find_element_by_css_selector('#file')
    upload_file.send_keys(file_path)
    time.sleep(1)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    #print('@@@@', type(button),type(browser), browser, button, sep='@@@\n@@@')
    button.click()
    time.sleep(20)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
