Before starting to run the tests, it is necessary to install all the programs and libraries.
- Google Chrome is installed
- Pycharm Community Edition is installed
- Python is installed
- Open File -> Open - Final_Project
- It is installed from Python Packages from Pycharm: selenium, behave, behave-html-formatter and webdriver-manager
Command to run Final_Project in Terminal (located in the bottom bar of Pycharm):
behave -f html -o behave-report.html
After running the scenarios related to one of the functionalities, the generated report can be viewed.\
This command will open the report in the system's default software (usually the default browser).\
In the generated report, we will have colors to quickly identify the tests that passed and those that failed.\
Test scenarios that passed will be marked in green, and those that failed will be marked in red.