from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class YandexLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_LINKS = (By.CLASS_NAME, "Path-Item")


class Page(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_enter(self):
        search_field = self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)
        return search_field

    def check_suggest(self):
        suggest = self.find_element(YandexLocators.LOCATOR_YANDEX_SUGGEST)
        return suggest

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=5)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_links(self):
        all_list = self.find_elements(YandexLocators.LOCATOR_YANDEX_LINKS, time=5)
        search_links = [x.text for x in all_list if len(x.text) > 0]
        return search_links