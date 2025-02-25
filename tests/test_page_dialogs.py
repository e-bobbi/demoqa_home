import pytest
from selenium import webdriver
from pages.modal_dialogs import ModalDialogsPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_modal_elements(browser):
    modal_page = ModalDialogsPage(browser)

    modal_page.open()

    buttons_count = modal_page.get_buttons_count()
    assert buttons_count == 5, f"Ожидалось 5 кнопок, но найдено {buttons_count}"

def test_navigation_modal(browser):
    modal_page = ModalDialogsPage(browser)

    modal_page.open()
    modal_page.refresh_page()
    modal_page.click_icon()
    modal_page.go_back()
    modal_page.set_window_size(900, 400)
    modal_page.go_forward()

    current_url = modal_page.get_current_url()
    assert current_url == "https://demoqa.com/", f"Ожидался URL https://demoqa.com/, но получен {current_url}"

    page_title = modal_page.get_page_title()
    assert page_title == "ToolsQA", f"Ожидался title 'ToolsQA', но получен {page_title}"

    modal_page.set_window_size(1000, 1000)
