from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from seleniumbase import Driver


class Browser():
    chrome = Driver(browser="chrome", headless=False)
    chrome.maximize_window()
    chrome.implicitly_wait(2)

    def close(self):
        self.chrome.delete_all_cookies()
        self.chrome.quit()
