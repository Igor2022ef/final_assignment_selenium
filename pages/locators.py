from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form_1 = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductObjectLocators():
    add_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    check_price = (By.CSS_SELECTOR, ".price_color")
    view_basket = (By.CSS_SELECTOR, ".btn-group > a")

