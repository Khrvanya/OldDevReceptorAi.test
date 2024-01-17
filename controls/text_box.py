from controls.base_control import BaseControl
from selenium.webdriver.common.keys import Keys


class TextBox(BaseControl):
    def __init__(self, text_box_element):
        super().__init__(text_box_element)

    def fill_field(self, text):
        self.element.send_keys(text)

    def clean_field(self):
        self.element.clean()

    def is_enabled(self):
        self.element.is_enabled()

    def click(self):
        self.element.click()

    def click_on_enter(self):
        self.element.send_keys(Keys.ENTER)
