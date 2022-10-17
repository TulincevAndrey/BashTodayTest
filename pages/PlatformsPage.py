import time

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Platforms(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    event_main = "//div[@id='f-event']"
    event_online_education = "/html/body/div[1]/div/form/section/div[2]/div[1]/div[1]/div/div/div[5]/div/ul/li[4]/label"
    price_filer = "//div[@id='f-price']"
    price_minimum = "//input[@name='price_min']"
    price_maximum = "//input[@name='price_max']"
    price_submit_button = "/html/body/div[1]/div/form/section/div[2]/div[3]/div[2]/div/button[2]"
    date_filter = "//div[@id='f-date']"
    date_next_month = "/html/body/div[1]/div/form/section/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div[1]/table/thead/tr[2]/th[3]"
    date_event = "//td[@data-date='1668643200000']"
    start_time = "//input[@name='time_start']"
    start_time_time ="/html/body/div[5]/ul/li[16]"
    end_time = "//input[@name='time_end']"
    end_time_time = "/html/body/div[6]/ul/li[5]"
    date_submit_button = "/html/body/div[1]/div/form/section/div[2]/div[2]/div[2]/div/button[2]"
    more_filters = "//div[@id='f-more']"
    guests = "//input[@name='guests']"
    more_filters_submit_button = "/html/body/div[1]/div/form/section/div[2]/div[4]/div[2]/div/button[2]"
    chosen_platform = "/html/body/div[1]/div/section/div[2]/div/div[2]/div[1]/div/div[2]/a"
    #Finders

    def find_event_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.event_main)))

    def find_event_online_education(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.event_online_education)))

    def find_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filer)))

    def find_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_minimum)))

    def find_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_maximum)))

    def find_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_submit_button)))

    def find_date_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_filter)))

    def find_date_next_month(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_next_month)))

    def find_date_event(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_event)))

    def find_start_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.start_time)))

    def find_start_time_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_time_time)))

    def find_end_time(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.end_time)))

    def find_end_time_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.end_time_time)))

    def find_time_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_submit_button)))

    def find_more_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.more_filters)))

    def find_guests(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.guests)))

    def find_more_filter_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.more_filters_submit_button)))

    def find_chosen_platform(self):
        chosen_platform = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.chosen_platform)))
        return chosen_platform

    #Actions

    def click_event_main(self):
        self.find_event_main().click()

    def click_event_online_education(self):
        self.find_event_online_education().click()

    def click_price(self):
        self.find_price().click()

    def input_price_min(self, price_min):
        self.find_price_min().send_keys(price_min)

    def input_price_max(self, price_max):
        self.find_price_max().send_keys(price_max)

    def click_submit_button(self):
        self.find_submit_button().click()

    def click_date_filter(self):
        self.find_date_filter().click()

    def click_date_next_month(self):
        self.find_date_next_month().click()

    def click_date_event(self):
        self.find_date_event().click()

    def click_start_time(self):
        self.find_start_time().click()

    def click_start_time_time(self):
        self.find_start_time_time().click()

    def click_end_time(self):
        self.find_end_time().click()

    def click_end_time_time(self):
        self.find_end_time_time().click()

    def click_time_show_button(self):
        self.find_time_show_button().click()

    def click_more_filters(self):
        self.find_more_filters().click()

    def input_guests(self, guests):
        self.find_guests().send_keys(guests)

    def click_more_filters_submit_button(self):
        self.find_more_filter_submit_button().click()

    def assertion_chosen_platform_value(self, result):
        chosen_platform_value = self.find_chosen_platform()
        print(chosen_platform_value)
        self.assert_words(chosen_platform_value, result)

    def click_chosen_platform(self):
        self.find_chosen_platform().click()

    #Methods

    def find_event(self):
        self.click_event_main()
        self.click_event_online_education()

    def find_platfrom_price(self):
        self.click_price()
        self.input_price_min("2000")
        self.input_price_max("5000")
        time.sleep(5)
        self.click_submit_button()
    def submit_date(self):
        self.click_date_filter()
        self.click_date_next_month()
        self.click_date_event()
        self.click_start_time()
        self.click_start_time_time()
        self.click_end_time()
        self.click_end_time_time()
        self.click_time_show_button()
        self.click_more_filters()

    def submit_more_filters(self):
        self.click_more_filters()
        self.input_guests("7")
        self.click_more_filters_submit_button()

    def choose_platform(self):
        self.click_chosen_platform()

    def full_path(self):
        self.find_event()
        self.find_platfrom_price()
        self.submit_date()
        self.submit_more_filters()
        time.sleep(5)
        self.assertion_chosen_platform_value("Переговорная Воздух #4162")
        self.click_chosen_platform()
        time.sleep(5)


