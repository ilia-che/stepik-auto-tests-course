from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    button = browser.find_element_by_link_text(text)
    button.click()
    #time.sleep(15)
    first_name = browser.find_element_by_name("first_name")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_name("last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element_by_class_name("city")
    city.send_keys("Smolensk")
    country = browser.find_element_by_id("country")
    country.send_keys("Russia")
    button2 = browser.find_element(By.CLASS_NAME,"btn-default")
    #print('@@@@', type(button),type(browser), browser, button, sep='@@@\n@@@')
    button2.click()
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
