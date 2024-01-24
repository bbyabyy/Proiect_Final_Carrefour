from browser import Browser

import pages




def before_all(context):
    context.browser = Browser()
    context.home_page = pages.carrefour_home_page.Home_page()
    context.careers_page = pages.carrefour_careers_page.Careers_page()
    context.login_page = pages.carrefour_login_page.Login_page()
    context.basket_page =pages.carrefour_mybasket_page.My_basket()


def after_all(context):
    context.browser.close()