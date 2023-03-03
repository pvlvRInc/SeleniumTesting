from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_tab(self, index):
        return self.driver.switch_to.window(self.driver.window_handles[index])

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can't find element with {locator} locator."
        )

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_all_elements_located(locator),
            message=f"Can't find elements with {locator} locator."
        )
