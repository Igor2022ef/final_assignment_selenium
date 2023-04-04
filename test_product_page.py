import time
from .pages.product_page import ProductObject

def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.check_price_purchase()
    page.check_name_purchase()


#Для запуска в фаерфокс pytest -s --browser_name=firefox test_product_page.py



