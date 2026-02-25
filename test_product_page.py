import time
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ItemPage




@pytest.mark.parametrize('link',
["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    item_page = ItemPage(browser, browser.current_url)
    item_page.should_be_item_page()
    item_page.add_item_in_basket()
    item_page.solve_quiz_and_get_code()
    item_page.check_success_add()
    time.sleep(100)