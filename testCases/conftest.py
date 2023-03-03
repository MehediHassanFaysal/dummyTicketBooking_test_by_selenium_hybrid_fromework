from selenium import webdriver
import pytest

########### Webdriver setup ###########
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.......")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.......")
    else:
        driver = webdriver.Ie
        print("Default browser.......")

    return driver

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):             # This will return the browser value to setup method
    return request.config.getoption("--browser")



#############  PyTest HTML Report #####################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Dummy ticket booking'
    config._metadata['Module Name'] = 'Ticket Management'
    config._metadata['Tester'] = 'Faysal Sarder'
    config._metadata['Starting date'] = '13-03-2023'
    config._metadata['Ending date'] = ''

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):          # delete default option from report
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
