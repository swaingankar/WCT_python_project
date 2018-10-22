import json
from test_suit.functional.automated.component.environmentsetup  import setUp

def safehand_admin_portal(i):
    driver = setUp(i)
    portal = open("test_suit/functional/json/portal.json","r",encoding="utf-8")
    url = json.load(portal)
    driver.get(
        url['Port']['httpsport'] + url['Instance']['InstanceName'] + url['Web']['safehandweb'] + url['Login'][
            'core'])  # Open Cofig Portal
    browser_name = driver.capabilities['browserName']
    if (browser_name == 'internet explorer'):
        driver.get("javascript:document.getElementById('overridelink').click();")
    print(browser_name)
    driver.implicitly_wait(20)
    driver.maximize_window()  # Maximize the Browser Window
    portal.close()
    return driver

def finance_portal(i):
    driver = setUp(i)
    portal = open("test_suit/functional/json/portal.json","r",encoding="utf-8")
    url = json.load(portal)
    driver.get(url['Port']['httpsport'] + url['Instance']['InstanceName'] + url['Web']['safehandweb'] + url['Login'][
            'finance'])  # Open Cofig Portal
    browser_name = driver.capabilities['browserName']
    if (browser_name == 'internet explorer'):
        driver.get("javascript:document.getElementById('overridelink').click();")
    print(browser_name)
    driver.implicitly_wait(20)
    driver.maximize_window()  # Maximize the Browser Window
    portal.close()
    return driver

def report_portal(i):
    driver = setUp(i)
    portal = open("test_suit/functional/json/portal.json","r",encoding="utf-8")
    url = json.load(portal)
    driver.get(url['Port']['httpsport'] + url['Instance']['InstanceName'] + url['Web']['safehandweb'] + url['Login'][
            'report'])  # Open Cofig Portal
    browser_name = driver.capabilities['browserName']
    if (browser_name == 'internet explorer'):
        driver.get("javascript:document.getElementById('overridelink').click();")
    driver.implicitly_wait(20)
    driver.maximize_window()  # Maximize the Browser Window
    return driver

def servicerequest_portal(i):
    driver = setUp(i)
    portal = open("test_suit/functional/json/portal.json","r",encoding="utf-8")
    url = json.load(portal)
    driver.get(
        url['Port']['httpsport'] + url['Instance']['InstanceName'] + url['Web']['safehandweb'] + url['Login'][
            'servicerequest'])  # Open Cofig Portal
    browser_name = driver.capabilities['browserName']
    if (browser_name == 'internet explorer'):
        driver.get("javascript:document.getElementById('overridelink').click();")
    print(browser_name)
    driver.implicitly_wait(20)
    driver.maximize_window()  # Maximize the Browser Window
    return driver

def land_doc_portal(i):
    driver = setUp(i)
    portal =  open("test_suit/functional/json/portal.json","r",encoding="utf-8")
    url = json.load(portal)
    driver.get(
        url['Port']['httpsport'] + url['Instance']['InstanceName'] + url['Web']['lb'] + url['Login'][
            'land'])  # Open Cofig Portal
    browser_name = driver.capabilities['browserName']
    if (browser_name == 'internet explorer'):
        driver.get("javascript:document.getElementById('overridelink').click();")
    print(browser_name)
    driver.implicitly_wait(20)
    driver.maximize_window()  # Maximize the Browser Window
    return driver

