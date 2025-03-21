from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class OnboardingPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    # Actions
    def CheckCurrencyVals(self,country='ES'):
        currencyMap = {'ES':'€','UK':'£','US':'$'}
        Bal_text = self.get_element_text("id","com.monefy.app.lite:id/balance_amount")
        if Bal_text[8] == currencyMap[country]:
            return True
        else:
            return False


