import json
from time import sleep
import pytest
from selenium import webdriver
import unittest
import yaml
# from self import self

from test_suit.functional.automated.component.environment_ie import EnvironmentSetUp_Ie

# @pytest.mark.skip(reason = "i don't want to test")
# class TryLoginWithInvalidPassword(EnvironmentSetUp_Ie):
# def test_login_web(self):
#     driver = EnvironmentSetUp_Ie.setUp(self)
#     portal = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\portal.json", "r",
#                   encoding="utf-8")
#     element_locator = open(
#         "C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\elementlocator.json", "r",
#         encoding="utf-8")
#     cred = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\credentials.json", "r",
#                 encoding="utf-8")
#     validation = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\validation.yaml",
#                       "r", encoding="utf-8")
#     url = json.load(portal)
#     credentials = json.load(cred)
#     locator = json.load(element_locator)
#     valid = yaml.load(validation)
#     driver.get(
#         url['Port']['httpsport'] + url['Instance']['InstanceName'] + url['Web']['safehandweb'] + url['Login'][
#             'core'])  # Open Cofig Portal
#     browser_name = driver.capabilities['browserName']
#     # if (browser_name == 'internet explorer'):
#     #     driver.get("javascript:document.getElementById('overridelink').click();")
#     print(browser_name)
#     driver.implicitly_wait(20)
#     # if(browser_name!='internet explorer'):
#     driver.maximize_window()  # Maximize the Browser Window
#     driver.find_element_by_xpath(
#         locator['Locator']['Login_Portal']['user_id']).send_keys(
#         credentials['Credentials']['sausername'])  # Find the username field in the page and fill the login id
#     sleep(4)
#     driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(
#         credentials['Credentials']['sapassword'])  # Find the password field in the page and fill the password
#     sleep(4)
#     driver.find_element_by_xpath(locator['Locator']['Login_Portal']['config_log_btn']).click()
#     sleep(2)
#     # elem = driver.find_element_by_xpath("//*[contains(text(),'Super Admin')]").text
#     elem = driver.find_element_by_xpath(valid['validation']['Safehand_admin']).text
#     print(elem)
#     valids = valid['validation']['admin_valid']
#     print(valids)
#     portal.close()
#     element_locator.close()
#     cred.close()
        # portal = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\portal.json", "r", encoding="utf-8")
        # element_locator = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\elementlocator.json", "r", encoding="utf-8")
        # cred = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\credentials.json", "r",
        #             encoding="utf-8")
        # loginerror = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\loginerror.json", "r",
        #                   encoding="utf-8")
        # url = json.load(portal)
        # credentials = json.load(cred)
        # locator = json.load(element_locator)
        # error = json.load(loginerror)
        # driver.get(url['Port']['httpsport']+url['Instance']['InstanceName']+url['Web']['safehandweb']+url['login']['core'])  # Open Cofig Portal
        # print(driver.title)
        # browser_name = driver.capabilities['browserName']
        # if (browser_name == 'internet explorer'):
        #     driver.get("javascript:document.getElementById('overridelink').click();")
        # driver.implicitly_wait(20)
        # driver.maximize_window()  # Maximize the Browser Window
        # driver.get_screenshot_as_file("C:\\Users\\WCT\\PycharmProjects\\LoginConfig\\screenshots\\login_2.png")
        # driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['sausername'])   # Find the username field in the page and fill the login id
        # sleep(2)
        # driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(credentials['Credentials']['invalidpassword'])  # Find the password field in the page and fill the password
        # sleep(2)
        # driver.find_element_by_xpath(locator['Locator']['Login_Portal']['config_log_btn']).click()
        # elem = driver.find_element_by_xpath("//*[contains(text(),'login failed. Username and/or password do not match')]").text
        # sleep(2)
        # portal.close()
        # cred.close()
        # element_locator.close()
        # # assert elem== error['Error']['invalidpassword']
        # loginerror.close()

# if __name__ == "__main__":
#     test_login_web(self)

# if __name__ == "__main__":
#   TryLoginWithInvalidPassword.test_login_web(self)


# import yaml
#
# validation = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\validation.yaml", "r",
#                   encoding="utf-8")
#
# valid = yaml.load(validation)
#
# print(valid['validation']['reports']);
#
#
#



























