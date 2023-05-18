import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Cart_page(Base):

    """Главная страницa Lamoda"""

    def __init__(self, driver):
        super().__init__(driver)
        self.move = ActionChains(self.driver)
        self.driver = driver

    """Locators"""

    total_price = "(//div[@class='_value_149e5_17']/span)[2]"
    button_checkout = "//div[@class='_buttonBackground_spx5p_6']/button"
    pickup_point = "//div[@class='_pickupSelect_1vp21_23']/button"
    pickup_point_smolenskaya_6 = "//div[text()='Lamoda | Москва | м. Смоленская | Смоленская, 6']"
    button_pick_up_here = "//div[@class='_submit_1vs6x_103']/button"
    first_name = "//input[@id='first_name']"
    last_name = "//input[@id='last_name']"
    phone = "//input[@id='phone']"
    email = "//input[@id='email']"
    check_box_news_and_sales = "//div[@class='x-checkbox__content']"

    """Getters"""

    def  get_total_price(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def  get_button_checkout(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def  get_pickup_point(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_point)))

    def get_pickup_point_smolenskaya_6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_point_smolenskaya_6)))

    def get_button_pick_up_here(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_pick_up_here)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_check_box_news_and_sales(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_news_and_sales)))

    """Actions"""

    def text_total_price(self):
        self.get_total_price().get_attribute('textContent')
        print("Price on Cart Page is " + self.get_total_price().get_attribute('textContent'))

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("Click button checkout")

    def click_pickup_point(self):
        self.get_pickup_point().click()
        print("Click pickup point")

    def click_pickup_point_smolenskaya_6(self):
        self.get_pickup_point_smolenskaya_6().click()
        print("Click pickup point Smolenskaya 6")

    def click_button_pick_up_here(self):
        self.get_button_pick_up_here().click()
        print("Click button pick up here")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def click_check_box_news_and_sales(self):
        self.get_check_box_news_and_sales().click()
        print("Click check box news and sales")

    """Methods"""

    def process_checkout(self):
        self.assert_url("https://www.lamoda.ru/checkout/cart/")
        self.text_total_price()
        self.click_button_checkout()
        self.click_pickup_point()
        self.click_pickup_point_smolenskaya_6()
        self.click_button_pick_up_here()
        self.input_first_name("Christina")
        self.input_last_name("Kordo-sysoeva")
        self.input_phone("9996663334")
        self.click_check_box_news_and_sales()
        self.click_button_checkout()




