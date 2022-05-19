from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchItemPage:
    # Search Page
    txtSearch_xpath = "//*[@id='container']//following::input[@title='Search for products, brands and more']"
    btnSearch_xpath = "//*[@id='container']//following::button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def searchitemlist(self, item):
        elem = self.driver.find_element_by_xpath(self.txtSearch_xpath)
        self.driver.implicitly_wait(2)
        elem.clear()
        self.driver.implicitly_wait(5)
        elem.send_keys(item)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()
        txtSearchResults_xpath = "//*[@id='container']//following::span[contains(text(),'" + item + "')]"
        getlist = self.driver.find_element_by_xpath(txtSearchResults_xpath)
        return getlist
