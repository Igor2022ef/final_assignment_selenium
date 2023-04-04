import time
from .pages.product_page import ProductObject

# Отрицательные тесты
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductObject(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductObject(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductObject(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(5)
    page.should_disappeared_message()




#Для запуска в фаерфокс pytest -s --browser_name=firefox test_product_page.py



