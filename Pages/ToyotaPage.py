from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import configReader


class toyotaPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, configReader.readConfig("Locators", "title_toyota_xpath")).text
