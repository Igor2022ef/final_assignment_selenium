from .base_page import BasePage
from .locators import ProductObjectLocators



class ProductObject(BasePage):
    def go_to_basket(self):
        button = self.browser.find_element(*ProductObjectLocators.add_basket)
        button.click()
    def check_price_thing(self):
        input1=self.browser.find_element(*ProductObjectLocators.check_price)
        y=input1.text[1:]
        print(y)
    def view_basket(self):
        button = self.browser.find_element(*ProductObjectLocators.view_basket)
        button.click()




