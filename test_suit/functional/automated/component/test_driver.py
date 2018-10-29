from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


class Driver:
    @staticmethod
    def chrome():
        options = Chrome_Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        print("Chrome has started !!!")
        return driver
    @staticmethod
    def ie():
        driver = webdriver.Ie()
        return driver
    @staticmethod
    def firefox():
        options = Firefox_Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        print("Firefox has started !!!")
        return driver


print(Driver.firefox())
