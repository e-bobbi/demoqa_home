import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent

class TestCheckText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://demoqa.com/')

    def test_footer_text(self):
        footer_locator = (By.CSS_SELECTOR, 'footer span')
        base_component = BaseComponent(self.driver)

        footer_text = base_component.get_text(footer_locator)

        self.assertEqual(footer_text, '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')

    def test_center_text_on_elements_page(self):
        elements_button_locator = (By.CSS_SELECTOR, '.card-body h5')
        base_component = BaseComponent(self.driver)

        base_component.find_element(elements_button_locator).click()

        center_text_locator = (By.CSS_SELECTOR, '.main-header')

        center_text = base_component.get_text(center_text_locator)

        self.assertEqual(center_text, 'Please select an item from left to start practice.')

    def tearDown(self):
        self.driver.quit()

if name == "__main__":
    unittest.main()
