from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class YandexLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_YANDEX_SUGGEST = (By.XPATH, "//ul[@class='mini-suggest__popup-content']")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_LINKS = (By.CLASS_NAME, "Path-Item")

    LOCATOR_YANDEX_HOME_BUTTON = (By.CLASS_NAME, "services-pinned__all")
    LOCATOR_YANDEX_IMAGES_BUTTON = (By.XPATH, "//a[@aria-label='Картинки']")
    LOCATOR_YANDEX_IMAGE_CATEGORIES = (By.CLASS_NAME, "PopularRequestList-Item")
    LOCATOR_YANDEX_IMAGES = (By.CLASS_NAME, "serp-item__link")
    LOCATOR_YANDEX_OPENED_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_IMAGE_OPEN_BUTTON = (By.XPATH, "//a[contains(@class, 'MMViewerButtons-OpenImage')]")
    LOCATOR_YANDEX_NEXT_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_YANDEX_PREVIOUS_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")

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

    def get_navigation_bar_text(self):
        elements = self.find_elements(YandexLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_text = [x.text for x in elements if len(x.text) > 0]
        return nav_bar_text

    def get_links_text(self):
        elements = self.find_elements(YandexLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        search_links_text = [x.text for x in elements if len(x.text) > 0]
        return search_links_text

    def get_home_button(self):
        home_button = self.find_element(YandexLocators.LOCATOR_YANDEX_HOME_BUTTON)
        return home_button

    def click_home_button(self):
        home_button = self.find_element(YandexLocators.LOCATOR_YANDEX_HOME_BUTTON)
        home_button.click()
        return home_button

    def click_images_button(self):
        images_button = self.find_element(YandexLocators.LOCATOR_YANDEX_IMAGES_BUTTON)
        images_button.click()
        return images_button

