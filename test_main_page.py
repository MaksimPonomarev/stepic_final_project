import time

import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators


link = "http://selenium1py.pythonanywhere.com/"
link_on_login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_success_transition_in_basket()
    page.should_be_empty_basket()
    page.should_be_empty_basket_message()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = BasketPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.should_be_login_link()