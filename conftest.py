from pytest import fixture
from selenium import webdriver


@fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe")
    yield driver
    driver.quit()
