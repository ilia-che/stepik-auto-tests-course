from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link1 = "https://www.mvideo.ru/products/multivarka-redmond-rmc-m224s-20052086"
    browser = webdriver.Chrome('/Users/admin/Downloads/chromedriver')
    # открываем страницу первого товара
    browser.get(link1)
    # закрываем всплывающие окна и прочее
    time.sleep(1)
    close_list = browser.find_elements_by_class_name("modal-layout__close")
    for close in close_list:
        close.click()
    print(close_list)
    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector(".mv-main-button--primary")
    time.sleep(1)
    add_button.click()
    time.sleep(1)
    # открываем страницу второго товара
    find_space = browser.find_element_by_class_name("input__field")
    find_space.click()
    find_space.send_keys("Ноутбук")
    time.sleep(5)
    find_result = browser.find_element_by_css_selector("ul.search-results-container li")
    find_result.click()
    time.sleep(5)
    close_list = browser.find_elements_by_class_name("close")
    for close in close_list:
        close.click()
    print(close_list)
    # добавляем товар в корзину
    time.sleep(5)
    add_button = browser.find_element_by_css_selector("[title='Добавить в корзину']")
    add_button.click()
    # тестовый сценарий
    # открываем корзину
    time.sleep(5)
    browser.get("https://www.mvideo.ru/cart")
    time.sleep(15)
    # ищем все добавленные товары
    goods = browser.find_elements_by_css_selector(".c-cart-item__header")
    # проверяем, что количество товаров равно 2
    assert len(goods) == 2
    print('@@@@', type(add_button),type(browser), browser, add_button, type(browser.get), sep='@@@\n@@@')
    time.sleep(5)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
