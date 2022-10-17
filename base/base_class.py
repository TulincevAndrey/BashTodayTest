import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method assert words"""

    def assert_words(self, words, result):
        value_words = words.text
        assert value_words == result
        print("Assertion OK")

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'Screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\pocht\\PycharmProjects\\BashTodayBusinessPath\\screen\\' + name_screenshot)