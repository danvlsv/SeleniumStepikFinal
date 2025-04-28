from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()