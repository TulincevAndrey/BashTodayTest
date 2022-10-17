import time

from selenium.webdriver import Keys

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class ChosenPlarform(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    send_request = "/html/body/div/div/section/div[2]/div/div[2]/div/form/button"
    send_button = "/html/body/div[1]/div/div[6]/div/div/div[3]/div[2]/button[2]"
    # Finders

    def find_send_request(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_request)))

    def find_send_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_button)))

    # Actions

    def click_send_request(self):
        self.find_send_request().click()

    def assert_send_button(self, result):
        send_button_value = self.find_send_button()
        self.assert_words(send_button_value, result)

    # Methods
    def chosen_platform(self):
        self.get_screenshot()
        self.click_send_request()
        self.assert_send_button("Отправить")
        time.sleep(10)
