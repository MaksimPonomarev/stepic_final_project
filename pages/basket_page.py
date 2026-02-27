from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasketPageLocators
from pages.main_page import MainPage
from pages.base_page import BasePage


class BasketPage(BasePage):
        def __init__(self, browser, url):
            self.browser = browser
            self.url = url


        def check_success_transition_in_basket(self):
            assert "basket" in self.browser.current_url

        def should_be_empty_basket(self):
            self.should_be_empty_basket_message()
            self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY)


        def should_be_empty_basket_message(self):
            wait = WebDriverWait(self.browser, 5)
            string_empty_basket = wait.until(EC.presence_of_element_located(BasketPageLocators.EMPTY_BASKET_MESSAGE))
            assert "basket is empty" in string_empty_basket.text, "'basket is empty' not in EMPTY_BASKET_MESSAGE"