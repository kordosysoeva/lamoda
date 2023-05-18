import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Main_page(Base):

    """Главная страницa Lamoda"""

    def __init__(self, driver):
        super().__init__(driver)
        self.move = ActionChains(self.driver)
        self.driver = driver

    """Locators"""

    brands = "//a[@href='/brands/?genders=women&sitelink=topmenuW&l=6']"
    brand_nike = "//a[@href='/lp/nike_w/?sitelink=topmenuW&l=11']"


    """Getters"""

    def  get_brands(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.brands)))

    def  get_brand_nike(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.brand_nike)))

    """Actions"""


    def move_to_brand(self):
        self.move.move_to_element(self.get_brands()).perform()
        print("Cursor over Brands")

    def click_brand_nike(self):
        self.get_brand_nike().click()
        print("Click brand nike")


    """Methods"""

    def choose_brand_nike(self):
        self.assert_url("https://www.lamoda.ru/women-home/")
        self.move_to_brand()
        self.click_brand_nike()


