from appium.webdriver.common.appiumby import AppiumBy
import time
from pages.base_page import BasePage

class IncomeExpenditurePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators later will be added in a folder
    BUTTON_1 = "com.monefy.app.lite:id/buttonKeyboard1"
    BUTTON_2 = "com.monefy.app.lite:id/buttonKeyboard2"
    BUTTON_3 = "com.monefy.app.lite:id/buttonKeyboard3"
    BUTTON_4 = "com.monefy.app.lite:id/buttonKeyboard4"
    BUTTON_ADD = "com.monefy.app.lite:id/buttonKeyboardPlus"
    BUTTON_EQUAL = "com.monefy.app.lite:id/buttonKeyboardEquals"
    RESULT_FIELD = "com.monefy.app.lite:id/amount_text"
    Choose_Category = "com.monefy.app.lite:id/keyboard_action_button"
    Salary_Category = '(//android.widget.ImageView[@resource-id="com.monefy.app.lite:id/imageView"])[2]'

    # Actions
    def add_income(self):
        """Click on Income button"""
        self.click_element("id", "com.monefy.app.lite:id/income_button")

        self.click_element("id",self.BUTTON_1)
        self.click_element("id",self.BUTTON_4)
        self.click_element("id",self.BUTTON_ADD)
        self.click_element("id",self.BUTTON_3)
        self.click_element("id",self.BUTTON_EQUAL)
        result = self.get_element_text("id",self.RESULT_FIELD)
        if result == "17":
            return True
        else:
            return False

    def add_expense(self):
        """Need Explicit wait to let the unintractable toast fade away"""
        #self.wait_to_disappear("id","com.monefy.app.lite: id / snackbar_text",20)
        self.click_element("id", "com.monefy.app.lite:id/expense_button")

        self.click_element("id",self.BUTTON_1)
        self.click_element("id",self.BUTTON_2)
        self.click_element("id",self.BUTTON_ADD)
        self.click_element("id",self.BUTTON_4)
        self.click_element("id",self.BUTTON_EQUAL)
        result = self.get_element_text("id",self.RESULT_FIELD)
        if result == "16":
            return True
        else:
            return False

    def get_category(self):
        self.click_element("id", self.Choose_Category)
        self.click_element("xpath",self.Salary_Category)

    def get_balance(self,balAmt):
        balance = self.get_element_text("id","com.monefy.app.lite:id/balance_amount")
        balance = balance.split('Balance $')[1]
        if balance == balAmt:
            return True
        else:
            return False

    def verify_note(self,text):
        self.input_text("id","com.monefy.app.lite:id/textViewNote",text)
        note = self.get_element_text("id","com.monefy.app.lite:id/textViewNote")
        if note == text:
            return True
        else:
            return False

