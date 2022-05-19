from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WelcomePage:
    txtSearch_xpath = "//*[@id='container']//following::input[@title='Search for products, brands and more']"
    btnSearch_xpath = "//*[@id='container']//following::button[@type='submit']"
    txtSearchResults_xpath = "//*[@id='container']//following::span[contains(text(),'Laptop')]"

    def __init__(self, driver):
        self.driver = driver

    def menuItems(self, menu):
        self.driver.implicitly_wait(0)
        text_menu_xpath = "//*[@id='container']//following::div[contains(text(),'" + menu + "')]"
        return self.driver.find_element(By.XPATH,text_menu_xpath)

