from pages.main_page import MainPage

def test_guest_open_login_form(browser):
    link = "https://www.saucedemo.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_button()