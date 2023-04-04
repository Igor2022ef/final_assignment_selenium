import time
from .pages.product_page import ProductObject
import pytest

# Отрицательные тесты
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()
    page.add_to_basket()

    """
    Товар из корзины сам не пропадает, поэтому в чистом виде срабатываение assert в этом методе не увидеть, 
    если раскомментить строку ниже, то будет падать из-за тогт, что товар в корзине, AssertionError увидим
    и еще увидим метку XPASS
    """
    # page.solve_quiz_and_get_code()
    page.should_disappeared_message()


#Для запуска в фаерфокс pytest -s --browser_name=firefox test_product_page.py



