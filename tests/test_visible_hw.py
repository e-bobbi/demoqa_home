import time
import pytest
from selenium import webdriver
from pages.accordion import Accordion

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # или любой другой браузер
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.open()

    assert accordion_page.section1_content().is_displayed(), "Элемент #section1Content > p должен быть виден"

    accordion_page.section1_heading().click()

    time.sleep(2)

    assert not accordion_page.section1_content().is_displayed(), "Элемент #section1Content > p не должен быть виден после клика"


import pytest
from selenium import webdriver
from pages.accordion import Accordion

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # или любой другой браузер
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.open()

    # Проверка, что элементы скрыты по умолчанию
    assert not accordion_page.section2_content_p1().is_displayed(), "Элемент #section2Content > p:nth-child(1) должен быть скрыт"
    assert not accordion_page.section2_content_p2().is_displayed(), "Элемент #section2Content > p:nth-child(2) должен быть скрыт"
    assert not accordion_page.section3_content_p().is_displayed(), "Элемент #section3Content > p должен быть скрыт"
