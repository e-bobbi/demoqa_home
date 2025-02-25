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
