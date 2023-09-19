import logging
import pytest
from Pages.RegistrationPage import RegistrationPage
from TestCases.BaseTest import BaseTest
from Utilities.dataProvider import get_data
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class Test_SignUpTest(BaseTest):
    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password", get_data("LoginTest"))
    def test_dosignup(self, name, phoneNum, email, country, city, username, password):
        regpage = RegistrationPage(self.driver)
        regpage.fillForm(name, phoneNum, email, country, city, username, password)
        # Create a log
        log.logger.info("Test Do Signup successfully " )

# in order to execute this test in paralel
# install
#pip install pytest-xdist
# The last is the number of paralell executions
#pytest test_WebdriverIntegration.py -n 3
# or you can set it in pytest.ini
#addopts = -n3
