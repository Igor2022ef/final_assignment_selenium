from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form_1 = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductObjectLocators():
    add_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    #Имя желаемого товара
    name_wished_thing = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] > h1")
    #Цена желаемого товара
    price_wished_thing = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] [class='price_color']")
    #Проверка названия товара в корзине
    check_name_in_basket = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    # Проверка цены товара в корзине
    check_price_in_basket = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > '
                                              'div > p:nth-child(1) > strong')
    #Нажимаем кнопку Посмотреть что в коризине, верхний левый угол стр.
    view_basket = (By.CSS_SELECTOR, ".btn-group > a")

