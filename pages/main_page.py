from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser
from pages.locators import BasketPageLocators
from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_view_basket_btn(self):
        wait = WebDriverWait(self.browser, 10)
        assert wait.until(EC.element_to_be_clickable(MainPageLocators.VIEW_BASKET_BTN)), "view_basket_btn not clicable"


