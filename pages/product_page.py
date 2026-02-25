from conftest import browser
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
        assert "promo" in self.browser.current_url, "url does not include 'promo=newYear'"

    def should_be_add_to_basket_btn(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(ItemPageLocators.BTN_ADD_TO_BASKET), "btn add to basket is not presented")

    def add_item_in_basket(self):
        basket_btn = self.browser.find_element(*ItemPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()

    def check_success_add(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(ItemPageLocators.MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK))
        list_of_web_elements = self.browser.find_elements(*ItemPageLocators.MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK)

        list_of_messages = []
        for element in list_of_web_elements:
            list_of_messages.append(element.text)

        wait.until(EC.visibility_of_element_located(ItemPageLocators.BOOK_NAME))
        book_name = self.browser.find_element(*ItemPageLocators.BOOK_NAME).text
        book_cost = self.browser.find_element(*ItemPageLocators.BOOK_COST).text
        assert book_name in list_of_messages, "different book add"
        assert book_cost in list_of_messages, "different cost added book"