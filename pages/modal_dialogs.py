from selenium.webdriver.common.by import By

class ModalDialogsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/modal-dialogs"
        self.buttons_locator = (By.CLASS_NAME, "btn-primary")

    def open(self):
        self.driver.get(self.url)

    def get_buttons_count(self):
        return len(self.driver.find_elements(*self.buttons_locator))
