import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Card_product_page(Base):

    """Главная страницa Lamoda"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    list_size = "//div[@class='_placeholder_1widv_51 _placeholderDisabled_1widv_98']"
    size_365 = "//div[text()='36,5 RUS']"
    button_add_to_cart = "//div[@class='recaptcha _recaptcha_lrjtr_7']/button"
    price_card_page = "//div[@class='_title_153ob_2']/span"
    redirect_to_cart = "//div[@class='d-modal__bottom']/a"

    """Getters"""

    def get_list_size(self):
        return WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.list_size)))

    def get_size_365(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_365)))

    def get_price_card_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_card_page)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver,  30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_redirect_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.redirect_to_cart)))

    """Actions"""

    def click_list_size(self):
        self.get_list_size().click()
        print("Click list size")

    def click_size_365(self):
        self.get_size_365().click()
        print("Click size 36.5")

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Click button add to cart")

    def text_price_my_favorite_shoes(self):
        self.get_price_card_page().get_attribute('textContent')
        print("Price on Card Page is " + self.get_price_card_page().get_attribute('textContent'))

    def click_redirect_to_cart(self):
        self.get_redirect_to_cart().click()
        print("Click button redirect_to_cart")


    """Methods"""

    def choose_size(self):

        self.assert_url("https://www.lamoda.ru/p/rtlack622401/shoes-nike-krossovki/")
        self.click_list_size()
        self.text_price_my_favorite_shoes()
        self.assert_price('15 890 ₽', self.get_price_card_page().get_attribute('textContent'))
        self.click_size_365()
        self.click_button_add_to_cart()
        self.click_redirect_to_cart()





