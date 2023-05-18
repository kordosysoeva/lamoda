import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Nike_preview_page(Base):

    """Главная страницa бренда Nike"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    category_run = "//a[@href='https://www.lamoda.ru/cb/4004-2047/default-sport_women_run-nike/?sf=231&sitelink=nike_w&l=4p1']"

    """Getters"""

    def  get_category_run(self):
        return  WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.category_run)))


    """Actions"""

    def click_category_run(self):
        self.get_category_run().click()
        print("Click category run")


    """Methods"""

    def choose_category_run(self):
        self.get_current_url()
        self.click_category_run()
