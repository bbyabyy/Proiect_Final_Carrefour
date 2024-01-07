from basepage import Base_page
from selenium.webdriver.common.by import By


class Login_page(Base_page):

    LOGIN_PAGE = "https://www.carrefour.ro/customer/account/login"
    EMAIL_ADDRESS = (By.ID, "credentials")
    PASSWORD = (By.ID, "pass")
    ENTER_THE_ACCOUNT = (By.ID, "send2")
    MY_ACCOUNT = (By.XPATH, '//span[@class="base" and @data-ui-id="page-title-wrapper"]')

    def __init__(self):
        self.chrome = None

    def navigate_to_homepage(self):
        self.chrome.get(self.LOGIN_PAGE)

    def insert_username(self, username):
        username = "contul.meu20@yahoo.com"
        self.chrome.find_element(*self.EMAIL_ADDRESS).send_keys(username)

    def insert_password(self, password):
        password = "_A#YcveC*Mrds5Q"
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_on_enter(self):
        self.chrome.find_element(*self.ENTER_THE_ACCOUNT).click()

    def open_account_page(self):
        self.chrome.find_element(*self.MY_ACCOUNT)