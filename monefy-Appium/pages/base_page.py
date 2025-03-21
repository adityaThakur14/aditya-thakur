from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    log = logging.INFO

    def find_element(self,locator_type, locator_value, timeout=10):

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )

    def get_element_attribute(self, locator_type, locator_value, attribute, timeout=10):
        """Fucntion to get attributes of an element"""
        element = self.find_element(locator_type, locator_value, timeout)
        return element.get_attribute(attribute)

    def click_element(self, locator_type, locator_value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()

    def tap_element(self, locator_type, locator_value):
        element = self.find_element(locator_type, locator_value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def input_text(self,locator_type,locator_value, text, timeout=10):
        element = self.find_element(locator_type,locator_value)
        element.send_keys(text)


    def scroll_to_text(self, text):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("{text}")')

    def get_element_text(self, locator_type, locator_value):
        """Get text of an element."""
        return self.find_element(locator_type, locator_value).text

    def wait_to_disappear(self,locator_type,locator_value,time=10):
        """Wait for an element to disappear from the screen."""
        logging.info("Waiting for element ({locator_type}, {locator_value}) to disappear...")
        self.wait.until(EC.invisibility_of_element_located((locator_type, locator_value)))
        print("Element disappeared!")
