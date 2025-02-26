from selenium.webdriver.common.by import By

def test_login_form_validate(browser):
    browser.get("https://demoqa.com/automation-practice-form")

    fields = {
        "firstName": "First Name",
        "lastName": "Last Name",
        "userEmail": "name@example.com"
    }

    for field_id, expected_placeholder in fields.items():
        input_field = browser.find_element(By.ID, field_id)
        assert input_field.get_attribute("placeholder") == expected_placeholder, f"Плейсхолдер для {field_id} неверный"

    email_input = browser.find_element(By.ID, "userEmail")
    expected_pattern = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    assert email_input.get_attribute("pattern") == expected_pattern, "Атрибут pattern у поля Email неверный"

    browser.find_element(By.ID, "submit").click()

    form = browser.find_element(By.ID, "userForm")
    assert "was-validated" in form.get_attribute("class"), "Класс 'was-validated' отсутствует у формы"
