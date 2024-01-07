from basepage import Base_page
from selenium.webdriver.common.by import By


class Home_page(Base_page):

    SEARCH_BOX = (By.ID, "search")
    SEARCH_BUTTON = (By.CLASS_NAME, "form-submit")
    SEARCH_RESULTS = (By.XPATH, '//h1[@class="page-title"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@role="button" and @title="Log in / Register"]')
    CAREERS_LINK = (By.XPATH, '//a[@href= "/corporate/cariere" and @title="Cariere">Ca]')
    ADD_TO_BASKET = (By.XPATH, '//button[@data-id="33524051"]')

    def __init__(self):
        self.chrome = None

    def navigate_to_homepage(self):
        self.chrome.get("https://www.carrefour.ro/")

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys(product_name)

    def click_on_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_search_results(self, results_number):
        no_results = self.chrome.find_element(*self.SEARCH_RESULTS).text()
        result = no_results.replace(",", "")
        assert int(result) >= int(results_number), (f"ERROR: Results Number is incorrect. EXPECTED: "
                                                    f"{results_number}, ACTUAL {result}")

    def insert_the_search_value(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys("cafea boabe")

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def add_to_bascket_button(self):
        self.chrome.find_element(*self.ADD_TO_BASKET).click()

    def click_on_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def click_on_carers_link(self):
        self.chrome.find_element(*self.CAREERS_LINK).click()