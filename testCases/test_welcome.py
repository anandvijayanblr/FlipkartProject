#############################################################################################################
# """
# Project :    Flipkart
# TestName: WelcomePage Test
# Authors: Anand Vijayan
# Modified On: 08-September 2021
# Description: To perform UI Test for Welcome Page
# Commands:
# Running Testcase Use command:
#     pytest -v -s testCases/test_welcome.py --browser chrome
# Running Testcases parallel:
#     pytest -v -s n=2 testCases/test_welcome.py --browser chrome
# Generate html report:
#     pytest -v -s --html=Reports\testreport.html testCases/test_welcome.py --browser chrome
# Running Testsuite:
#     pytest -v -s -m "regression or sanity" --html=Reports\testreport.html testCases/ --browser chrome
# Running allure report:
#     command prompt : allure generate result --clean -o report
#     pytest -v -s --alluredir="C:\Users\anand\Desktop\FlipkartProject\Reports\result" testCases/test_welcome.py --browser chrome
# """
#############################################################################################################


import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.WelcomePage import WelcomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import TestLog


@allure.severity(allure.severity_level.NORMAL)
class TestCase_001_Welcome:
    testLogs = TestLog.CreateLog()
    baseURL = ReadConfig.getWebURL()
    list = ["Grocery", "Mobiles", "Fashion"]

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_welcomePage(self, setup):

        self.testLogs.info("***************** TestCase_001_WelcomePage is Started ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//button[@class = '_2KpZ6l _2doB4z']").click()
        self.driver.maximize_window()

        act_title = self.driver.title
        if act_title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. " \
                        "Best Offers!":
            assert True
            self.testLogs.info("TestCase_001_WelcomePage : Passed")
        else:
            assert False
            allure.attach(self.driver.get_screenshot_as_png(), name="testWelcomePage",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_welcomePageTitle.png")
            self.testlog.error("TestCase_001_WelcomePage:Failed")
        self.driver.close()
        self.testLogs.info("***************** TestCase_001_WelcomePage is Completed ******************")

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_welcomeMenu(self, setup):
        self.testLogs.info("***************** TestCase_001_WelcomeMenu is Started ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//button[@class = '_2KpZ6l _2doB4z']").click()
        self.driver.maximize_window()
        self.wp = WelcomePage(self.driver)

        for i in range(0, len(self.list)):
            result = self.wp.menuItems(self.list[i])
            if result:
                assert True
                self.testLogs.info("TestCase_001_welcomeMenu : Passed")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="testWelcomeMenu",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_welcomeMenu.png")
                assert False
                self.testLogs.error("TestCase_001_welcomeMenu:Failed")
        self.driver.close()

        self.testLogs.info("***************** TestCase_001_WelcomeMenu is Completed ******************")
