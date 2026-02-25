from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username[required]")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password[required]")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type=submit][name=login_submit]")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email[required]")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1[required]")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2[required]")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "button[type=submit][name=registration_submit]")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ItemPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_OF_SUCCESS_ADD_SELECTED_BOOK = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_COST = (By.CSS_SELECTOR, "p.price_color")