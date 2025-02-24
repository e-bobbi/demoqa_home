from selenium.webdriver.common.by import By

class Accordion:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://demoqa.com/accordian"

    def open(self):
        self.browser.get(self.url)

    def section1_content(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#section1Content > p")

    def section1_heading(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#section1Heading")

# from selenium.webdriver.common.by import By

# class Accordion:
#     def __init__(self, browser):
#         self.browser = browser
#         self.url = "https://demoqa.com/accordian"

#     def open(self):
#         self.browser.get(self.url)

#     def section1_content(self):
#         return self.browser.find_element(By.CSS_SELECTOR, "#section1Content > p")

#     def section1_heading(self):
#         return self.browser.find_element(By.CSS_SELECTOR, "#section1Heading")

#     def section2_content_p1(self):
#         return self.browser.find_element(By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")

#     def section2_content_p2(self):
#         return self.browser.find_element(By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")

#     def section3_content_p(self):
#         return self.browser.find_element(By.CSS_SELECTOR, "#section3Content > p")
