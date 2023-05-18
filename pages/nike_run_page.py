import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Nike_run_page(Base):

    """Cтраницa бренда Nike -категория Бег"""

    def __init__(self, driver):
        super().__init__(driver)
        self.move = ActionChains(self.driver)
        self.driver = driver

    """Locators"""

    filter_by_popularity = "//span[text()='По популярности']"
    radio_button_hight_price = "(//div[@class='_item_g6flk_14'])[3]"
    filter_by_materials = "//span[text()='Материалы']"
    check_box_top = "(//span[text()='текстиль'])[1]"
    check_box_inside = "(//span[text()='текстиль'])[2]"
    button_accept = "//button[text()='Применить']"
    filter_by_color = "//span[text()='Цвет']"
    check_box_black_color = "//span[text()='черный']"
    filter_by_size = "//span[text()='Размер']"
    check_box_size_365 = "//span[text()='36,5']"
    filter_by_price = "//span[text()='Цена']"
    min_price = "//input[@name='minRange']"
    max_price = "//input[@name='maxRange']"
    price_my_favorite_shoes = "(//span[@style='white-space: nowrap;'])[1]"
    img_shoes = "//a[@href='/p/rtlack622401/shoes-nike-krossovki/']"


    """Getters"""
    def get_filter_by_popularity(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.filter_by_popularity)))

    def get_radio_button_hight_price(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.radio_button_hight_price)))

    def get_filter_by_materials(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_by_materials)))

    def get_check_box_top(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_top)))

    def get_check_box_inside(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_inside)))

    def get_button_accept(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_accept)))

    def get_filter_by_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_by_color)))

    def get_check_box_black_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_black_color)))

    def get_filter_by_size(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_by_size)))

    def get_check_box_size_365(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_size_365)))

    def get_filter_by_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_by_price)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_price_my_favorite_shoes(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_my_favorite_shoes)))

    def get_img_shoes(self):
        return self.driver.find_element(By.XPATH, self.img_shoes)

    """Actions"""

    def click_filter_by_popularity(self):
        self.get_filter_by_popularity().click()
        print("Click filter by popularity")

    def click_radio_button_hight_price(self):
        self.get_radio_button_hight_price().click()
        print("Click radio button hight price")

    def click_filter_by_materials(self):
        self.get_filter_by_materials().click()
        print("Click filter by materials")

    def click_check_box_top(self):
        self.get_check_box_top().click()
        print("Click check box top")

    def click_check_box_inside(self):
         self.get_check_box_inside().click()
         print("Click check_box_inside")

    def click_button_accept(self):
        try:
            time.sleep(1)
            self.get_button_accept().click()
            print("Click button_accept")
        except StaleElementReferenceException as exception:
            time.sleep(2)
            self.get_button_accept().click()
            print("Get exception")


    def click_filter_by_color(self):
        self.get_filter_by_color().click()
        print("Click filter_by_color")

    def click_check_box_black_color(self):
        time.sleep(1)
        self.get_check_box_black_color().click()
        print("Click check_box_black_color")

    def click_filter_by_size(self):
        time.sleep(1)
        self.get_filter_by_size().click()
        print("Click filter_by_size")

    def click_check_box_size_365(self):
        self.get_check_box_size_365().click()
        print("Click check_box_size_365")

    def click_filter_by_price(self):
        self.get_filter_by_price().click()
        print("Click filter_by_price")

    def input_min_price(self, price):
        time.sleep(1)
        self.get_min_price().send_keys(Keys.BACKSPACE * 10)
        self.get_min_price().send_keys(price)
        print("Input min price")

    def input_max_price(self, price):
        time.sleep(1)
        self.get_max_price().send_keys(Keys.BACKSPACE * 10)
        self.get_max_price().send_keys(price)
        print("Input max price")

    def text_price_my_favorite_shoes(self):
        time.sleep(1)
        self.get_price_my_favorite_shoes().get_attribute('textContent')
        print("Price on Nike Run Page is " + self.get_price_my_favorite_shoes().get_attribute('textContent'))

    def move_to_img_shoes(self):
        time.sleep(1)
        self.move.move_to_element(self.get_img_shoes()).perform()
        self.get_img_shoes().click()
        print("Click on img")

    """Methods"""

    def filtering_settings(self):
        self.get_current_url()
        self.click_filter_by_popularity()
        self.click_radio_button_hight_price()
        self.click_filter_by_materials()
        self.click_check_box_top()
        self.click_check_box_inside()
        self.click_button_accept()
        self.click_filter_by_color()
        self.click_check_box_black_color()
        self.click_button_accept()
        self.click_filter_by_size()
        self.click_check_box_size_365()
        self.click_button_accept()
        self.click_filter_by_price()
        self.input_min_price(6000)
        self.input_max_price(16000)
        self.click_button_accept()
        self.text_price_my_favorite_shoes()
        self.move_to_img_shoes()







