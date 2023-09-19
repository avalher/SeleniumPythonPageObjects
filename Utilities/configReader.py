from configparser import ConfigParser

"""""
#set the reader
config = ConfigParser()
#file config to read
config.read("config.ini")
#read the keys: config.get("section", "key")
print(config.get("locator", "username"))
#utility to read the file
"""


def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\config.ini")
    return config.get(section, key)


#print(readConfig("locators","name_css"))


"""""
option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

driver = webdriver.Chrome(options=option)
driver.get('https://www.makemytrip.com/')
driver.implicitly_wait(5)
driver.switch_to.frame("notification-frame-~10cb443b6")
locator = readConfig("locator", "username")
# for this only need to put the '' in the config file to the locator
driver.find_element(By.XPATH, locator).click()
driver.switch_to.default_content()
"""
