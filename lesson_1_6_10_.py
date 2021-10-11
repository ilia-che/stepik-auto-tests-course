from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"  # подставляем адрес нужной страницы
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')  # если нужн, прописываем путь до chromedriver
    browser.get(link)
    time.sleep(3)
    # ищем поля по уникальным селекторам, при этом проверяя их обязательность(наличие тега required)
    first_name = browser.find_element_by_css_selector('input.first[required]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector('input.second[required]')
    last_name.send_keys("Petrov")
    e_mail = browser.find_element_by_css_selector("input.third[required]")
    e_mail.send_keys("i.p@smolensk.ru")
    # смотрим на результат либо падаем в ошибку NoSuchElementException(ловить не стал, т.к. в задании не просят)
    time.sleep(3)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()  # нажми на кнопку - получишь результат)))
    time.sleep(5)
    welcome_text = browser.find_element_by_tag_name("h1").text
    assert welcome_text == 'Congratulations! You have successfully registered!'
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    # P.S. успехов в грядущих автотестах
