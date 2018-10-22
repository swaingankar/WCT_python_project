from selenium import webdriver


class Driver:
    @staticmethod
    def chrome():
        driver = webdriver.Chrome()
        return driver
    @staticmethod
    def ie():
        driver = webdriver.Ie()
        return driver
    @staticmethod
    def firefox():
        driver = webdriver.Firefox()
        return driver
