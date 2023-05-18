import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.card_product_page import Card_product_page
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.nike_preview_page import Nike_preview_page
from pages.nike_run_page import Nike_run_page


def test_buy_product_1():
    options = Options().add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Kristina\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    print("Start test 1")

    try:
        lp = Login_page(driver)
        lp.authorization_with_gmail()
        mp = Main_page(driver)
        mp.choose_brand_nike()
        npp = Nike_preview_page(driver)
        npp.choose_category_run()
        nrp = Nike_run_page(driver)
        nrp.filtering_settings()
        cpp = Card_product_page(driver)
        cpp.choose_size()
        cp = Cart_page(driver)
        cp.process_checkout()
        time.sleep(10)

    except TimeoutException as exception:
        while exception:
            lp = Login_page(driver)
            lp.authorization_with_gmail()
            mp = Main_page(driver)
            mp.choose_brand_nike()
            npp = Nike_preview_page(driver)
            npp.choose_category_run()
            nrp = Nike_run_page(driver)
            nrp.filtering_settings()
            cpp = Card_product_page(driver)
            cpp.choose_size()
            cp = Cart_page(driver)
            cp.process_checkout()
