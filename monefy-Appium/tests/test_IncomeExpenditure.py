import pytest
import allure
from pages.base_page import BasePage
from pages.IncomeExpenditure_page import IncomeExpenditurePage


@pytest.mark.run(order=4)
@allure.title("Test to add Income in monefy app")
@allure.description("This test verifies if user is able to record income in app")
@pytest.mark.usefixtures("wait_after_test")
def test_04_add_income(base_page):
    incExp = IncomeExpenditurePage(base_page)
    with allure.step("Go to Income field and input income by addition"):
        assert incExp.add_income(), "Error in adding Incomes"
    with allure.step("Add notes for the Income earned"):
        assert incExp.verify_note("Hourly Income")
    with allure.step("Select category for Incomes"):
        incExp.get_category(), "Error in selecting category"
    with allure.step("Compare result in Balance field"):
        assert incExp.get_balance("17.00"), "Error in adding income to Balance field"


@pytest.mark.run(order=5)
@allure.title("Test to add Expenditure in monefy app")
@allure.description("This test verifies if user is able to record expenses in the app")
@pytest.mark.usefixtures("wait_after_test")
def test_05_add_expense(base_page):
    incExp = IncomeExpenditurePage(base_page)
    with allure.step("Go to expense field and input expense by addition"):
        assert incExp.add_expense(), "Error in adding Expenses"
    with allure.step("Add notes for the expense incurred"):
        assert incExp.verify_note("Misc Expenses")
    with allure.step("Select category for Expenses"):
        incExp.get_category(), "Error in selecting category"
    with allure.step("Compare result in Balance field"):
        assert incExp.get_balance("1.00"), "Error in adding expense to Balance field"




