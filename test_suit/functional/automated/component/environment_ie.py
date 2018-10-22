import datetime
import unittest
from test_suit.functional.automated.component.test_driver import Driver


class EnvironmentSetUp_Ie(unittest.TestCase):
    def setUp_ie(self):
        driver = Driver.chrome()  # Open the Chrome Browser
        print("Run Started at : " + str(datetime.datetime.now()))
        print("------------------------------------------------------------------")
        driver.implicitly_wait(20)
        return driver
    def tearDown_ie(self):
        print("--------------------------------------------------------")
        print("Ie Environment Destroyed")
        print("Run Completed at : " + str(datetime.datetime.now()))
        self.driver.quit()
