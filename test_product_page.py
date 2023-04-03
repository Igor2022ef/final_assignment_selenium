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


#Отрицательные тесты
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#     page = ProductObject(browser, link)
#     page.open()
#     page.go_to_basket()
#     page.should_not_be_success_message()
#     #Здесь следует написать метод проверки, что товар в корзине
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#     page = ProductObject(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#     page = ProductObject(browser, link)
#     page.open()
#     page.go_to_basket()
#     page.should_disappeared_message()




#Для запуска в фаерфокс pytest -s --browser_name=firefox test_product_page.py



