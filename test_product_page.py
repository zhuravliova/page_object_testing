from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.take_product_name()
    page.take_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_product()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



@pytest.mark.xfail(reason="guest may see success")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()


@pytest.mark.xfail(reason="message must be visible after adding product to basket")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(1)
    page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
