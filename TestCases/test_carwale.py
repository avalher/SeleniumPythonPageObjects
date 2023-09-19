import logging
import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Pages.RegistrationPage import RegistrationPage
from TestCases.BaseTest import BaseTest
from Utilities.dataProvider import get_data
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("****Inside new car test******")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle", get_data("newCarsTest"))
    def test_dosignup(self, carBrand, carTitle):
        log.logger.info("****Inside select new car test******")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car title is: "+title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"



    @pytest.mark.parametrize("carBrand, carTitle", get_data("newCarsTest"))
    def test_printcarnameandprice(self, carBrand, carTitle):
        log.logger.info("****Inside Car Names and prices******")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()

