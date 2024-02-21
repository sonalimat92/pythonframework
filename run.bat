behave -f allure_behave.formatter:AllureFormatter -o Report\allure_result -D browser=%Browser%
allure generate Report\allure_result -o Report\allure_report --clean