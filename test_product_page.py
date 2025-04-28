from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

import pytest
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.check_correct_product()

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.check_success_msg_is_not_present()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message(browser,link):
    page = ProductPage(browser, link)
    page.open()
    assert page.check_success_msg_is_not_present()

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.check_success_msg_dissapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, link)
    assert basket_page.basket_is_empty()

@pytest.mark.xfail
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, link)
    assert basket_page.basket_is_not_empty()

@pytest.mark.user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser,link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        pswrd = "pasw_"+str(time.time())
        page.register_new_user(email,pswrd)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        assert page.check_success_msg_is_not_present()

    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert page.check_correct_product()