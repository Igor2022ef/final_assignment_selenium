import time
from .pages.product_page import ProductObject

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_basket()
    # time.sleep(5)
    page.solve_quiz_and_get_code()
    page.check_price_thing()
    page.view_basket()
    # time.sleep(10)

#Для запуска в фаерфокс pytest -s --browser_name=firefox test_product_page.py



