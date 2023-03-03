from page.yandex_page import Page


def test_yandex_search(browser):
    ya_page = Page(browser)
    ya_page.go_to_site()

    ya_page.enter_word("Тензор")
    suggest = ya_page.check_suggest()
    assert bool(suggest)
    ya_page.press_enter()

    nav_bar_elements_text = ya_page.get_navigation_bar_text()
    assert 'Поиск' and 'Картинки' in nav_bar_elements_text

    links = ya_page.get_links_text()
    assert 'tensor.ru' == links[0]


def test_yandex_images(browser):
    ya_page = Page(browser)
    ya_page.go_to_site()

    home_button = ya_page.get_home_button()
    assert bool(home_button)

    home_button.click()
    ya_page.click_images_button()
    ya_page.switch_tab(1)
    current_url = ya_page.get_current_url()
    assert current_url == "https://yandex.ru/images/"

    first_category = ya_page.get_categories()[0]
    first_category.click()
    search_field_text = ya_page.get_search_field_text()
    assert search_field_text == first_category.text
