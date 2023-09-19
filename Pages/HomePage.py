from Pages.BasePage import BasePage
from Pages.newCarsPage import newCarPage


class HomePage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newcar_xpath")
        self.click("findNewCars_xpath")

        return newCarPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass
