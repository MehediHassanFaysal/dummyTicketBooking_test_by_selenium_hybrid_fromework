import time

import pytest
from selenium import webdriver
from pageObjects.DummyTicketBooking import dummy
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_RadioButton:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()   # obj of LogGen class

    try:
        def test_homePageTitle(self, setup):
            self.logger.info("*********** Test_001_RadioButton ***********")
            self.logger.info("*********** Verifying Home Page Title ***********")
            self.driver = setup
            self.driver.get(self.baseURL)
            actual_title = self.driver.title

            if actual_title == "Dummy ticket for applying visa - Verifiable flight reservation for embassy":
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
                self.driver.close()
                assert False
    except:
        print("Runtime problem on verifying the home page title.......")

    try:
        def radioButton_test(self, setup):
            self.driver = setup
            self.driver.get(self.baseURL)
            self.dm = dummy(self.driver)
            self.dm.clickOnvisaApplication()
            time.sleep(2)
            if self.dm.expectedValue() == '"Dummy ticket for Visa Application" added to your order. Complete your order below.':
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\"+"VisaApplicationRadioButton.png")
                print(self.dm.expectedValue())
                assert False
                self.driver.close()

    except:
        print("Rantime problem on checking the visa application of radio button")
