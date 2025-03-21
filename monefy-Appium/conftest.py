from base.common import get_resource_config
import os
from collections import namedtuple
import pytest
import allure
from base.web_drivers import WebDriver
from pages.base_page import BasePage
import logging
import time

logging.basicConfig(  format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)


"""
def pytest_configure(config):
  
    os.environ["ROOT_PATH"] = config.rootdir.strpath
    config.option.cacheclear = True
    config.option.capture = "sys"  # no: for no output at all
    config.option.clean_alluredir = True
    config.option.color = "yes"
    config.option.disable_warnings = True
    config.option.instafail = True
    config.option.failedfirst = True
    config.option.json_report_indent = 2
    config.option.json_report_omit = ["warnings"]
    config.option.json_report = True
    config.option.maxfail = 1
    config.option.pythonwarnings = ["ignore:Unverified HTTPS request"]
    config.option.tbstyle = "short"
    config.option.self_contained_html = True
    config.option.verbose = 1

    #if config.getoption("allure_report_dir") is None:
    #    config.option.allure_report_dir = f"allure-results"

"""


@allure.feature("Launch App")
@allure.story("Verify app launches and click on get started works")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture(scope='session')
def set_driver():
    driver = WebDriver.get_appiumdriver()

    yield driver
    try:
        driver.driver.close()
    except (Exception, ValueError):
        pass

@pytest.fixture()
def base_page(set_driver):
    return BasePage(set_driver)

@pytest.fixture()
def wait_after_test():
    """Adds a hard wait after each test."""
    yield  # Run the test first
    wait_time = 20
    if wait_time:
        logging.info(f"Waiting for {wait_time} seconds before proceeding...")
        time.sleep(wait_time)
