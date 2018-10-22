# import json
# from time import sleep
# import pytest
# from test_suit.functional.automated.component.test_environmentsetup import EnvironmentSetUp
#
# @pytest.mark.skip(reason = "i don't want to test")
# class TryLoginallWithInvalidUsername(EnvironmentSetUp):
#     def test_login_web(self):
#         driver = self.driver
#         portal = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\portal.json", "r",
#                       encoding="utf-8")
#         element_locator = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\elementlocator.json", "r",
#             encoding="utf-8")
#         cred = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\credentials.json", "r",
#                     encoding="utf-8")
#         loginerror = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\loginerror.json", "r",
#                           encoding="utf-8")
#         url = json.load(portal)
#         credentials = json.load(cred)
#         locator = json.load(element_locator)
#         error = json.load(loginerror)
#         driver.get(url['Port']['httpsport']+url['Instance']['InstanceName']+url['Web']['safehandweb']+url['Login']['core'])  # Open Cofig Portal
#         print(driver.title)
#         driver.implicitly_wait(20)
#         driver.maximize_window()  # Maximize the Browser Window
#         driver.get_screenshot_as_file("C:\\Users\\WCT\\PycharmProjects\\LoginConfig\\screenshots\\login_2.png")
#         driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['invalidusername'])   # Find the username field in the page and fill the login id
#         sleep(2)
#         driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(
#             credentials['Credentials']['sapassword'])  # Find the password field in the page and fill the password
#         sleep(2)
#         driver.find_element_by_xpath(locator['Locator']['Login_Portal']['config_log_btn']).click()
#         elem = driver.find_element_by_xpath("//*[contains(text(),'login failed. Username and/or password do not match')]").text
#         sleep(2)
#         portal.close()
#         element_locator.close()
#         cred.close()
#         assert elem== error['Error']['invalidpassword']
#         loginerror.close()
#
# if __name__ == "__main__":
#    EnvironmentSetUp.setUp()
