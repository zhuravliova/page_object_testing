from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE)

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE)

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE) 

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON)

    def should_be_message_about_adding_product(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def take_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text

    def take_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text
