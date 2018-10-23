import datetime

from test_suit.functional.automated.component.test_driver import Driver

def setUp(i):
    if i == "Chrome":
        driver = Driver.chrome() # Open the Chrome Browser
        driver.implicitly_wait(20)
        print("Run Started at : " + str(datetime.datetime.now()))
        print("Chrome Environment Set UP")
        print("------------------------------------------------------------------")
        return driver
    elif i == "IE":
        driver = Driver.ie()  # Open the Chrome Browser
        driver.implicitly_wait(20)
        print("Run Started at : " + str(datetime.datetime.now()))
        print("IE Environment Set UP")
        print("------------------------------------------------------------------")
        return driver
    else:
        driver = Driver.firefox()    # Open the Chrome Browser
        driver.implicitly_wait(20)
        print("Run Started at : " + str(datetime.datetime.now()))
        print("Firfox Environment Set UP")
        print("------------------------------------------------------------------")
        return driver
def tearDown(self):
    print("--------------------------------------------------------")
    print("Ie Environment Destroyed")
    print("Run Completed at : " + str(datetime.datetime.now()))
    self.driver.quit()

