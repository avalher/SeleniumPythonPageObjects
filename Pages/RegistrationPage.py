from Pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def fillForm(self, name, phoneNum, email, country, city, username, password):
        self.type("name_xpath", name)
        self.type("phone_xpath", phoneNum)
        self.type("email_xpath", email)
        self.select("country_xpath", country)
        self.type("city_xpath", city)
        self.type("username_xpath", username)
        self.type("password_xpath", password)
        self.click("submit_XPATH")


