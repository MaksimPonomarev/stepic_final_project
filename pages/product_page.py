from conftest import browser
from pages.locators import ProductPageLocators
from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def should_be_Product_page(self):
        self.should_be_Product_url()
        self.should_be_add_to_basket_btn()

    def should_be_Product_url(self):
        "promo" in self.browser.current_url, "url does not include 'promo'"

    def should_be_add_to_basket_btn(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(ProductPageLocators.BTN_ADD_TO_BASKET), "btn add to basket is not presented")

    def add_product_in_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()

    def check_success_add(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(ProductPageLocators.MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK))
        list_of_web_elements = self.browser.find_elements(*ProductPageLocators.MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK)

        list_of_messages = []
        for element in list_of_web_elements:
            list_of_messages.append(element.text)

        wait.until(EC.visibility_of_element_located(ProductPageLocators.BOOK_NAME))
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_cost = self.browser.find_element(*ProductPageLocators.BOOK_COST).text
        assert book_name in list_of_messages, "different book add"
        assert book_cost in list_of_messages, "different cost added book"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK), \
            "The success message did not disappear."