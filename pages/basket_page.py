from .locators import BasketLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def basket_is_empty(self):
        return (self.is_not_element_present(*BasketLocators.BASKET_FORM) or
                self.is_element_present(*BasketLocators.EMPTY_BASKET_MSG))

    def basket_is_not_empty(self):
        return (self.is_element_present(*BasketLocators.BASKET_FORM) and
                self.is_not_element_present(*BasketLocators.EMPTY_BASKET_MSG))
    # def empty_basket_mag(self):
    #     return self.is_element_present(*BasketLocators.EMPTY_BASKET_MSG)