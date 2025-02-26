import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_text_box(browser):
    browser.get("https://demoqa.com/text-box")

    full_name = "Евгений Бобылёв"
    current_address = "СПб, ул.Чапыгина, дом 9"

    browser.find_element(By.ID, "userName").send_keys(full_name)
    browser.find_element(By.ID, "currentAddress").send_keys(current_address)

    browser.find_element(By.ID, "submit").click()

    output_name = browser.find_element(By.ID, "name").text
    output_address = browser.find_element(By.ID, "currentAddress").text

    assert f"Name:{full_name}" in output_name, "Текст в поле Name не совпадает"
    assert f"Current Address :{current_address}" in output_address, "Текст в поле Current Address не совпадает"
