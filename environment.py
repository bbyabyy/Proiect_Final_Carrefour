from browser import Browser
from pages.carrefour_careers_page import Careers_page
from pages.carrefour_home_page import Home_page
from pages.carrefour_login_page import Login_page
from pages.carrefour_mybasket_page import My_basket


def before_all(context):
    context.browser = Browser()
    context.home_page = Home_page()
    context.careers_page = Careers_page()
    context.login_page = Login_page()
    context.basket_page = My_basket()


def after_all(context):
    context.browser.close()