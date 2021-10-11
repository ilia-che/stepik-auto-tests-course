from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/math.html'  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    time.sleep(1)

    # прожимаем чекбокс и радиобатн
    #check_box = browser.find_element_by_css_selector('#robotCheckbox').click()
    radio_button = browser.find_element_by_css_selector('#robotsRule')
    print(radio_button.get_attribute("checked"))
    lol = radio_button.get_attribute("checked")
    print(lol)
    kek = browser.find_element_by_css_selector('.form-check-custom')
    print("class:", kek.get_attribute('class'))
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    time.sleep(3)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()  # нажми на кнопку - получишь результат)))
    time.sleep(5)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    # P.S. успехов в грядущих автотестах
