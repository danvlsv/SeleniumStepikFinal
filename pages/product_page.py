from time import sleep

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()

    def check_correct_product(self):
        sleep(5)
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        result = self.browser.find_element(*ProductPageLocators.ADDED_NAME)
        assert expected.text==result.text

    def check_success_msg_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_NAME)

    def check_success_msg_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_NAME)