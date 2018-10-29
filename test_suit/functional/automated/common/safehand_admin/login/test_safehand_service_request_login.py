import jsonfrom time import sleepimport pytestimport yamlfrom test_suit.functional.automated.common.safehand_admin.login.portal import servicerequest_portal@pytest.mark.parametrize("i", ['Chrome','IE','Firefox'])def test_valid(i):    driver = servicerequest_portal(i)    element_locator = open("test_suit/functional/json/elementlocator.json", "r", encoding="utf-8")    cred = open("test_suit/functional/json/credentials.json", "r", encoding="utf-8")    validation = open("test_suit/functional/json/validation.yaml", "r", encoding="utf-8")    credentials = json.load(cred)    locator = json.load(element_locator)    valid = yaml.load(validation)    driver.find_element_by_xpath(        locator['Locator']['Login_Portal']['user_id']).send_keys(        credentials['Credentials']['clerk'])  # Find the username field in the page and fill the login id    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(        credentials['Credentials']['clpassword'])  # Find the password field in the page and fill the password    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['land_log_btn']).click()    sleep(2)    elem = driver.find_element_by_xpath(valid['validation']['servicerequest']).text    creds = valid['validation']['request_valid']    element_locator.close()    cred.close()    assert elem == creds    driver.quit()@pytest.mark.parametrize("i", ['Chrome','IE','Firefox'])def test_invalid_password(i):    driver = servicerequest_portal(i)    element_locator = open("test_suit/functional/json/elementlocator.json", "r", encoding="utf-8")    cred = open("test_suit/functional/json/credentials.json", "r", encoding="utf-8")    validation = open("test_suit/functional/json/validation.yaml", "r", encoding="utf-8")    credentials = json.load(cred)    locator = json.load(element_locator)    valid = yaml.load(validation)    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['sausername'])   # Find the username field in the page and fill the login id    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(credentials['Credentials']['invalidpassword'])  # Find the password field in the page and fill the password    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['land_log_btn']).click()    elem = driver.find_element_by_xpath(valid['validation']['invalid']).text    error1 = valid['validation']['invalidpassword']    sleep(2)    cred.close()    element_locator.close()    assert elem == error1    driver.quit()@pytest.mark.parametrize("i", ['Chrome','IE','Firefox'])def test_invalid_username(i):    driver = servicerequest_portal(i)    element_locator = open("test_suit/functional/json/elementlocator.json", "r", encoding="utf-8")    cred = open("test_suit/functional/json/credentials.json", "r", encoding="utf-8")    validation = open("test_suit/functional/json/validation.yaml", "r", encoding="utf-8")    credentials = json.load(cred)    locator = json.load(element_locator)    valid = yaml.load(validation)    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(credentials['Credentials']['invalidusername'])   # Find the username field in the page and fill the login id    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(        credentials['Credentials']['sapassword'])  # Find the password field in the page and fill the password    driver.find_element_by_xpath(locator['Locator']['Login_Portal']['land_log_btn']).click()    elem = driver.find_element_by_xpath(valid['validation']['invalid']).text    error1 = valid['validation']['invalidpassword']    sleep(2)    element_locator.close()    cred.close()    assert elem == error1    driver.quit()# if __name__ == "__main__":#     test_valid("IE")#             driver1 = webdriver#             driver1 = Portal.portals(self)#             element_locator = open(#                 "C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\elementlocator.json", "r",#                 encoding="utf-8")#             cred = open("C:\\Users\\WCT\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\credentials.json", "r",#                         encoding="utf-8")#             credentials = json.load(cred)#             locator = json.load(element_locator)#             driver1.get_screenshot_as_file("C:\\Users\\WCT\\PycharmProjects\\LoginConfig\\screenshots\\login_2.png")#             driver1.find_element_by_xpath(locator['Locator']['Login_Portal']['user_id']).send_keys(#                 credentials['Credentials']['sausername'])  # Find the username field in the page and fill the login id#             driver1.find_element_by_xpath(locator['Locator']['Login_Portal']['password']).send_keys(#                 credentials['Credentials']['sapassword'])  # Find the password field in the page and fill the password#             driver1.find_element_by_xpath(locator['Locator']['Login_Portal']['default_Log_btn']).click()#             sleep(2)#             elem = driver1.find_element_by_xpath("//*[contains(text(),'Super Admin')]").text#             element_locator.close()#             cred.close()#             assert elem == credentials['Credentials']['sa']## if __name__ == "__main__":#   t = test_LoginWithValidDetails#   t.test_login_web(self)