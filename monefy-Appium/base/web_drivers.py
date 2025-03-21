
from appium import webdriver
from appium.options.android import UiAutomator2Options



class WebDriver:

    @staticmethod
    def get_appiumdriver(device_name="emulator-5556"):
        options = UiAutomator2Options()
        options.platform_Name = 'Android'
        options.device_name = device_name
        options.app_package = "com.monefy.app.lite"
        options.app_activity = "com.monefy.activities.main.MainActivity_"
        options.no_reset = False
        options.automation_name = "UiAutomator2"
        driver = webdriver.Remote("http://localhost:4723", options= options)

        return driver


