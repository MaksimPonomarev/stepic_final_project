from pages.locators import ItemPageLocators
from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemPage(BasePage):
    def should_be_item_page(self):
        self.should_be_item_url()
        self.should_be_add_to_basket_btn()

    def should_be_item_url(self):
        assert "promo=newYear" in self.browser.current_url, "url does not include 'promo=newYear'"

    def should_be_add_to_basket_btn(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ItemPageLocators.BTN_ADD_TO_BASKET), "btn add to basket is not presented")

    def add_item_in_basket(self):
        basket_btn = self.browser.find_element(*ItemPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()