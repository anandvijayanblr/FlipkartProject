import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

selenium_grid_url = "http://localhost:4444"


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Remote(
        #     command_executor=selenium_grid_url,
        #     options=webdriver.ChromeOptions()
        # )

        ser = Service("chromedriver.exe")
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=op)
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['ProjectName'] = 'Flipkart'
    config._metadata['TestName'] = 'Search Product'
    config._metadata['Tested By'] = 'Anand Vijayan'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
    metadata.pop("Python", None)
