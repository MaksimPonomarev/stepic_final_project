from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        pass


    def should_be_login_button(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login-button"), "login button is not found"