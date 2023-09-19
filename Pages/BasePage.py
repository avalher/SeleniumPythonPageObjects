import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)
class BasePage:

    def __init__(self, driver):
        self.driver = driver
    #keywords
    def click(self, locator):
        if str(locator).endswith("_xpath"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_css"):
            self.driver.find_element(By.CSS, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_id"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click
        #Create a log
        log.logger.info("Clicking on a element: "+str(locator))
    def type(self, locator, value):
        if str(locator).endswith("_xpath"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_css"):
            self.driver.find_element(By.CSS, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_id"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing on a element: " + str(locator) + "value entered as: "+ str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_xpath"):
            dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_css"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_id"):
            dropdown = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("Selecting on a element: " + str(locator) + "value selected as: "+ str(value))

    def moveTo(self, locator):

        if str(locator).endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_id"):
            element = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Moving to an element: " + str(locator))

