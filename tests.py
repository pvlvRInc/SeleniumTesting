from page.yandex_page import Page


def test_yandex_search(browser):
    yandex_main_page = Page(browser)
    yandex_main_page.go_to_site()

    yandex_main_page.enter_word("Тензор")
    suggest = yandex_main_page.check_suggest()
    assert bool(suggest)
    yandex_main_page.press_enter()

    nav_bar_elements_text = yandex_main_page.get_navigation_bar_text()
    assert 'Поиск' and 'Картинки' in nav_bar_elements_text

    links = yandex_main_page.get_links_text()
    assert 'tensor.ru' == links[0]
