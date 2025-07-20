import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser',default='chrome')
    parser.addoption('--headless',action='store_true')
    parser.addoption('--url',default='https://automationexercise.com/')
@pytest.fixture(scope='function')
def driver(request):
    browser=request.config.getoption('--browser')
    headless=request.config.getoption('--headless')
    base_url=request.config.getoption('--url')
    if browser=='chrome':
        service_obj=Service('C:\\Drivers\\chromedriver.exe')
        options=Options()
        options.add_argument('--start-maximized')
        if headless:
            options.add_argument('--headless')
        driver=webdriver.Chrome(service=service_obj,options=options)
        driver.get(base_url)
    else:
        print('Except chrome browser, nthing works')
    yield driver
    driver.quit()
