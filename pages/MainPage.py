import time

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class MainPage(Base):
    url = 'https://bash.today/'
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    login_button = "/html/body/div[2]/header/nav/div/div[2]/ul[2]/li[2]/a"
    e_mail = "//input[@name='email']"
    password = "//input[@name='password']"
    log_button = "//button[@type='submit']"
    platforms_button = "/html/body/div[2]/header/nav/div/div[2]/ul/li[1]/a"
    #Finders
    def find_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def find_field_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail)))

    def find_field_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def find_log_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.log_button)))

    def find_platforms_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.platforms_button)))

        #Actions
    def click_login_button(self):
        self.find_login_button().click()

    def input_field_email(self, email):
        self.find_field_email().send_keys(email)

    def input_field_password(self, password):
        self.find_field_password().send_keys(password)

    def click_log_button(self):
        self.find_log_button().click()

    def click_platforms_button(self):
        self.find_platforms_button().click()

    #Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_button()
        self.input_field_email("tulincev.andrey@gmail.com")
        self.input_field_password("test_auto_123")
        self.click_log_button()
        self.click_platforms_button()
        time.sleep(3)