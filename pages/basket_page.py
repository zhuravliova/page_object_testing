from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE, timeout=1), "Basket not empty"

    def should_be_empty_basket(self):
        self.basket_is_empty()
        self.should_be_empty_basket_message()

    def should_be_empty_basket_message(self):
        assert not self.is_not_element_present(*BasketPageLocators.BASKET_INNER)
