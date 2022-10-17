from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.MainPage import MainPage
from pages.PlatformsPage import Platforms
from pages.ChosenPlatformPage import ChosenPlarform

def test_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\pocht\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)
    mp = MainPage(driver)
    mp.authorization() #login: tulincev.andrey@gmail.com     password: test_auto_123
    pp = Platforms(driver)
    pp.full_path()
    cpp = ChosenPlarform(driver)
    cpp.chosen_platform()