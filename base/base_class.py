import datetime
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Goood value word")


    """Method make screenshot"""

    def make_screen(self):
        now_date = datetime.datetime.today().strftime("%d.%m.%Y_%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Kristina\\PycharmProjects\\main_project\\screen\\' + name_screenshot)
        print("Make screen")

    """Method assert url"""

    def assert_url(self, result):
        time.sleep(1)
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method assert price"""

    def assert_price(self, first_price, second_price):
        assert first_price == second_price
        print("Price is identical")