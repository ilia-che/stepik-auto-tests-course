from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    browser.get(link)
    label_list = browser.find_elements_by_css_selector('label')
    input_list = browser.find_elements_by_css_selector('input')
    for i in range(len(label_list)):
        if label_list[i].text[-1]=='*':
            input_list[i].send_keys('Required')

    time.sleep(5)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    #print('@@@@', type(button),type(browser), browser, button, sep='@@@\n@@@')
    button.click()
    time.sleep(5)
    welcome_text = browser.find_element_by_tag_name("h1").text
    assert welcome_text == 'Congratulations! You have successfully registered!'
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
