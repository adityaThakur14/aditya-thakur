
Author == Aditya Thakur
Testing application:

git: https://github.com/swagger-api/swagger-petstore

I have chosen the User endpoint to test.

### How to start

By using Windows Terminal, Python and pip
1. Place the repository files into the directory of your choice
2. Create virtual environment

py -m venv env

2. Activate created virtual environment  

env\Scripts\activate

3. Install project's dependencies  

pip install -r requirements.txt


### How to run tests

- **Without Allure Test report**

All tests: pytest

Positive tests: pytest -m positive

Negative tests: pytest -m negative

- **With Allure Test report**

pytest --alluredir=allure_reports

Show generated report in browser: allure serve allure_reports

