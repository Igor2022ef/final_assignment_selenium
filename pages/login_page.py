import time
from .locators import MainPageLocators
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    #Посмотри, как рализовать декаротор внутри класса, видимо или классметод или статикметод
          #
          # self.helper1()
    #     self.wrapper()
    #
    # def helper1(func):
    #     def wrapper(*args, **kwargs):
    #         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #         login_link.click()
    #         res = func(*args, **kwargs)
    #         return res
    #     return wrapper
    #
    # @helper1

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(3)
        assert "login" in self.browser.current_url,  "login world not found"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина на странице
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(5)
        print({*LoginPageLocators.login_form_1})
        self.browser.find_element(*LoginPageLocators.login_form_1)
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(5)
        self.browser.find_element(*LoginPageLocators.register_form)
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "register form is not presented"



