import pytest
import allure
from pages.base_page import BasePage
from pages.Onboarding_page import OnboardingPage


@pytest.mark.run(order=1)
@allure.title("Test app launch")
@allure.description("This test verifies that the app is launched successfully with main page")
def test_01_launch_monefy(base_page):
    #set_driver.allure_attach_jpeg(file_name='homePage')
    with allure.step("Find the button and click it"):
        assert base_page.find_element("id","com.monefy.app.lite:id/buttonContinue")
    try:
        while base_page.find_element("id","com.monefy.app.lite:id/buttonContinue"):
            base_page.find_element("id","com.monefy.app.lite:id/buttonContinue").click()
    except:
        pass

@pytest.mark.run(order=2)
@allure.title("Test to check Offer Page")
@allure.description("This test verifies that if there is any offer page launched in app")
def test_02_checkOffer(base_page):
    with allure.step("Check for the offer page and click skip"):
        assert base_page.find_element("id","com.monefy.app.lite:id/buttonPurchase")
    try:
        if base_page.find_element("id","com.monefy.app.lite:id/buttonPurchase"):
            base_page.find_element("id","com.monefy.app.lite:id/buttonClose").click()
    except:
        pass


@pytest.mark.run(order=3)
@allure.title("Test to verify default currency")
@allure.description("This test verifies if default currency is picked upon the geo location")
def test_03_checkCurrency(base_page):
    onboarding = OnboardingPage(base_page)
    with allure.step("Check for the Balance amount units"):
        assert onboarding.CheckCurrencyVals('ES')
















