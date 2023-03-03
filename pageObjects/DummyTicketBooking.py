from selenium import webdriver
from selenium.webdriver.common.by import By


class dummy:
    radioButton_visaApplication_id = "product_549"
    expect_valueOf_radioButton_relXpath = "//div[@role='alert']"

    def __int__(self,driver):
        self.driver=driver

    def clickOnvisaApplication(self):
        self.driver.find_element(By.ID, self.radioButton_visaApplication_id).click()

    def expectedValue(self):
        self.driver.find_element(By.XPATH, self.expect_valueOf_radioButton_relXpath).text
