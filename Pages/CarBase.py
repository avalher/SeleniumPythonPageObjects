from selenium.webdriver.common.by import By

from Utilities import configReader


class CarBase:
    
    def __init__(self, driver):
        self.driver = driver


    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, configReader.readConfig("locators", "title_toyota_xpath")).text

    def getCarNameAndPrices(self):
        carNames = self.driver.find_elements(By.XPATH, configReader.readConfig("locators", "carName_xpath"))
        carPrices = self.driver.find_elements(By.XPATH, configReader.readConfig("locators", "carPrice_xpath"))
        #addinig comments
        for i in range(1, len(carPrices)):
            print(carNames[i].text+"----Prices are----"+carPrices[i].text)


