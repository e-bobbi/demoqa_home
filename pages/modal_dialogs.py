from selenium.webdriver.common.by import By

class ModalDialogsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/modal-dialogs"
        self.buttons_locator = (By.CLASS_NAME, "btn-primary")  
        self.icon_locator = (By.CSS_SELECTOR, "a[href='/']")

    def open(self):
        self.driver.get(self.url)

    def get_buttons_count(self):
        return len(self.driver.find_elements(*self.buttons_locator))

    def refresh_page(self):
        self.driver.refresh()

    def click_icon(self):
        self.driver.find_element(*self.icon_locator).click()

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title
