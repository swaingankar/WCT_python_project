import json
from time import sleep
import pytest
import yaml
from test_suit.functional.automated.common.safehand_admin.login.portal import safehand_admin_portal


@pytest.mark.parametrize("i", ['Chrome','IE','Firefox'])
def test_valid(i):

    driver = safehand_admin_portal(i)
    element_locator = open("test_suit/functional/json/elementlocator.json", "r", encoding="utf-8")
    cred = open("test_suit/functional/json/credentials.json", "r", encoding="utf-8")
    validation = open("test_suit/functional/json/validation.yaml", "r", encoding="utf-8")
    credentials = json.load(cred)
    locator = json.load(element_locator)
    valid = yaml.load(validation)
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['sausername'])  # Find the username field in the page and fill the login id
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(credentials['Credentials']['sapassword'])
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['config_log_btn']).click()
    sleep(2)
    elem = driver.find_element_by_xpath(valid['validation']['Safehand_admin']).text
    valids = valid['validation']['admin_valid']
    element_locator.close()
    cred.close()
    assert elem == valids
    driver.quit()


@pytest.mark.parametrize("i", ['Chrome','IE','Firefox'])
def test_invalid_password(i):
    driver = safehand_admin_portal(i)
    element_locator = open("test_suit/functional/json/elementlocator.json", "r", encoding="utf-8")
    cred = open("test_suit/functional/json/credentials.json", "r", encoding="utf-8")
    validation = open("test_suit/functional/json/validation.yaml", "r", encoding="utf-8")
    credentials = json.load(cred)
    locator = json.load(element_locator)
    valid = yaml.load(validation)
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['invalidusername'])  # Find the username field in the page and fill the login id
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(credentials['Credentials']['sapassword'])  # Find the password field in the page and fill the password
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['config_log_btn']).click()
    elem = driver.find_element_by_xpath(valid['validation']['invalid_admin']).text
    error1 = valid['validation']['invalidpassword']
    sleep(2)
    cred.close()
    element_locator.close()
    assert elem == error1
    driver.quit()


@pytest.mark.parametrize("i", ['Chrome','IE','Firefox'])
def test_invalid_username(i):
    driver = safehand_admin_portal(i)
    element_locator = open("test_suit/functional/json/elementlocator.json", "r", encoding="utf-8")
    cred = open("test_suit/functional/json/credentials.json", "r", encoding="utf-8")
    validation = open("test_suit/functional/json/validation.yaml", "r", encoding="utf-8")
    credentials = json.load(cred)
    locator = json.load(element_locator)
    valid = yaml.load(validation)
    driver.get_screenshot_as_file("C:\\Users\\SANTOSH\\PycharmProjects\\LoginConfig\\screenshots\\login_2.png")
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['sausername'])  # Find the username field in the page and fill the login id
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(
        credentials['Credentials']['invalidpassword'])  # Find the password field in the page and fill the password
    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['config_log_btn']).click()
    elem = driver.find_element_by_xpath(valid['validation']['invalid_admin']).text
    error1 = valid['validation']['invalidpassword']
    sleep(2)
    element_locator.close()
    cred.close()
    assert elem == error1
    driver.quit()






















