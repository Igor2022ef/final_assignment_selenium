from .base_page import BasePage
from .locators import ProductObjectLocators

class ProductObject(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductObjectLocators.add_basket)
        button.click()

    def check_price_purchase(self):
        input3 = self.browser.find_element(*ProductObjectLocators.price_wished_thing)
        price_product = input3.text
        input1=self.browser.find_element(*ProductObjectLocators.check_price_in_basket)
        price_purchase=input1.text
        assert price_purchase == price_product, "sad story: the price is not correct"

    def check_name_purchase(self):
        input4 = self.browser.find_element(*ProductObjectLocators.name_wished_thing)
        name_product = input4.text
        input2 = self.browser.find_element(*ProductObjectLocators.check_name_in_basket)
        name_purchase = input2.text
        # print(f"Имя товара: {name_product},{len(name_product)} ")
        # print(f"Имя покупки: {name_purchase[2:-31]}, {len(name_purchase[2:-31])}")
        assert name_product == name_purchase[2:-31], "sad story: the name is not correct"


    #Проверка, что элемент элемент не появляется на странице в течение заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductObjectLocators.check_name_in_basket), \
            "Success message is presented, but should not be"
    # Проверка, элемент исчезает со страницы в течение заданного времени
    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductObjectLocators.check_name_in_basket), \
           "Success message is disappeared, but should not be"





