from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url does not include 'login'"

    def should_be_login_form(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_FORM),"Login form is not presented")


    def should_be_register_form(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.REGISTER_FORM),"Register form is not presented")

