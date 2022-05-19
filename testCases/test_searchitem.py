#############################################################################################################
# """
# Project :    Flipkart
# TestName: Search Product Test
# Authors: Anand Vijayan
# Modified On: 08-September 2021
# Description: To perform UI and functionality Test for Product Search
# Commands:
# Running Testcase Use command:
#     pytest -v -s testCases/test_searchitem.py --browser chrome
# Running Testcases parallel:
#     pytest -v -s n=2 testCases/test_searchitem.py --browser chrome
# Generate html report:
#     pytest -v -s --html=Reports\testreport.html testCases/test_searchitem.py --browser chrome
# Running Testsuite:
#     pytest -v -s -m "regression or sanity" --html=Reports\testreport.html testCases/ --browser chrome
# Running allure report:
#     pytest -v -s --alluredir="C:\Users\anand\Desktop\FlipkartProject\Reports\result" testCases/test_searchitem.py --browser chrome
# """
#############################################################################################################

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.SearchItemPage import SearchItemPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import TestLog
from utilities import XLUtils


@allure.severity(allure.severity_level.NORMAL)
class TestCase_001_SearchItem:
    testLogs = TestLog.CreateLog()
    baseURL = ReadConfig.getWebURL()
    list = ["mobiles"]
    btnLoginCancel_xpath = "//button[@class='_2KpZ6l _2doB4z']"
    path = ".//TestData//ProductData.xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_searchItem(self, setup):
        self.testLogs.info("*****************DDT: TestCase_001_ProductSearch is Started ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']").click()
        self.driver.maximize_window()
        getLogin = self.driver.find_element_by_xpath(self.btnLoginCancel_xpath)
        if getLogin:
            self.driver.find_element_by_xpath(self.btnLoginCancel_xpath).click()
        self.sp = SearchItemPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'ProductDetails')

        for r in range(2,self.rows+1):
            self.Item = XLUtils.readData(self.path,'ProductDetails',r,1)
            result = self.sp.searchitemlist(self.Item)
            if result:
                assert True
                self.testLogs.info("TestCase_001_ProductSearch : Passed")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="testsearchItem",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_searchItem.png")
                assert False
                self.testLogs.error("TestCase_001_ProductSearch : Failed")
        self.driver.close()
        self.testLogs.info("*****************DDT: TestCase_001_ProductSearch is Completed ******************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_orderItem(self):
        pytest.skip('Skipped: Not Yet Implemented')
