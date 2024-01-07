from basepage import Base_page
from selenium.webdriver.common.by import By


class My_basket(Base_page):

    MY_BASKET_BUTTON = (By.XPATH, '//a[@role="button" and @title="minicart"]')
    REMOVE_BUTTON = (By.XPATH, '//div[@class="js-qty-update item-delete"]')
    ALERT_MESSAGE = (By.XPATH, '//div[@style= "display: block;"]')

    def __init__(self):
        self.chrome = None

    def click_on_my_basket(self):
        self.chrome.find_element(*self.MY_BASKET_BUTTON).click()

    def click_on_remove_button(self):
        self.chrome.find_element(*self.REMOVE_BUTTON).click()

    def alert_empty_cart(self):
        self.chrome.find_element(*self.ALERT_MESSAGE)