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

