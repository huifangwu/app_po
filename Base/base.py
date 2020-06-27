from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:
    def __init__(self):
        self.driver = Driver.get_app_driver()

    def find_ele(self, type, timeout=5, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*type))

    def find_eles(self, type, timeout=5, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*type))

    def click_ele(self, type, timeout=5, poll_frequency=1.0):
        self.find_ele(type, timeout, poll_frequency).click()

    def send_ele(self, type, text, timeout=5, poll_frequency=1.0):
        input_text = self.find_ele(type, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)
