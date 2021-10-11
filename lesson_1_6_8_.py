from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)
    first_name = browser.find_element_by_name("first_name")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_name("last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element_by_class_name("city")
    city.send_keys("Smolensk")
    country = browser.find_element_by_id("country")
    country.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//form/div/button[@type="submit"]')
    #print('@@@@', type(button),type(browser), browser, button, sep='@@@\n@@@')
    button.click()
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
