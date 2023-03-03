from page.yandex_page import Page


def test_yandex_search(browser):
    yandex_main_page = Page(browser)
    yandex_main_page.go_to_site()

    yandex_main_page.enter_word("Тензор")
    suggest = yandex_main_page.check_suggest()
    assert bool(suggest)