# MonefyApptest-Android
This is a framework repo for automating monefy android application using python with pytest and pom framework

**Pre Requisites**
1. Download and setup python3 from : https://www.python.org/downloads/
2. Before starting the tests install dependencies and appium 2 using the official documentation here : https://github.com/appium/appium
3. Install UiAutomator 2 plugin with Appium2 drivers

**Setup the framework and requirements and execute Test**
1. Go to project directory 
    `cd monefy-Appium`
2. Select the interpreter by going into preferences (No need if you are going to run tests from terminal) and create a virtual environment
3. Activate the virtual environment
    `source venv/bin/activate`
4. install python dependencies
    `pip install -r requirements.txt`
5. Run test using pytest command and tests directory with allure
    `pytest tests --aluredir=allure-results`
6. Get Allure report by running
   ` allure serve allure-results`

**Project Structure**
1. base - It contains all the appium drivers, common functions and workers functions
2. resources - It contains all the apk's and url configurations which will be used throughout the project
3. pages - It contains all the pages class and their methods to implement POM
4. tests - It contains the test class which needs to be triggered
5. allure_results - folder to save our allure report
    
    a. run `allure serve` to get the allure report on localhost
    
    b. run `allure generate` to generate a allure report and it will be saved under /allure-report

6. conftest - as it is heart of pytest, we will keep only fixture and pytest methods there
7. requirements.txt - contains all our dependency there and then download