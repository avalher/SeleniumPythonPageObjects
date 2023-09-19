from Pages.BasePage import BasePage


class newCarPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.click("hyundai_xpath")
    def selectBMW(self):
        self.click("bmw_xpath")

    def selectToyota(self):
        self.click("toyota_xpath")
    def selectHonda(self):
        self.click("honda_xpath")