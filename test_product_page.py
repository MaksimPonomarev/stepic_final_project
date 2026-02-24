import time

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ItemPage

link_on_item_page = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link_on_item_page)
    page.open()
    item_page = ItemPage(browser, browser.current_url)
    item_page.should_be_item_page()
    item_page.add_item_in_basket()
    item_page.solve_quiz_and_get_code()