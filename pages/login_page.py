from conftest import browser
from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url does not include 'login'"

    def should_be_login_form(self):
        assert self.browser.find_element(LoginPageLocators.LOGIN_EMAIL), "element 'LOGIN_EMAIL' not found"
        assert self.browser.find_element(LoginPageLocators.LOGIN_PASSWORD), "element 'LOGIN_PASSWORD' not found"
        assert self.browser.find_element(LoginPageLocators.LOGIN_BTN), "element 'LOGIN_BTN' not found"




    def should_be_register_form(self):
        assert self.browser.find_element(LoginPageLocators.REGISTRATION_EMAIL), "element 'REGISTRATION_EMAIL' not found"
        assert self.browser.find_element(LoginPageLocators.REGISTRATION_PASSWORD1), "element 'REGISTRATION_PASSWORD1' not found"
        assert self.browser.find_element(LoginPageLocators.REGISTRATION_PASSWORD2), "element 'REGISTRATION_PASSWORD2' not found"
        assert self.browser.find_element(LoginPageLocators.REGISTRATION_BTN), "element 'REGISTRATION_BTN' not found"