import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
# driver.set_window_size(1920,1080)

class Login_page(Base):

    """Авторизация на сайте Lamoda"""

    url = 'https://www.lamoda.ru/women-home/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    button_login_header = "//button[text()='Войти'] "
    button_gmail = "//span[@class='_item_1jtb3_12 _item_gp_1jtb3_26']"
    email  = "//input[@type='email']"
    button_continue = "(//button[@jsname='LgbsSe'])[2]"
    password = "//input[@type='password']"
    super =  "(//button[@type='button'])[3]"
    close_promo = "//div[@title='Закрыть']"

    """Getters"""

    def  get_button_login_header(self):
        return  WebDriverWait(self.driver,  5).until(EC.element_to_be_clickable((By.XPATH, self.button_login_header)))

    def  get_button_gmail(self):
        return  WebDriverWait(self.driver,  60).until(EC.element_to_be_clickable((By.XPATH, self.button_gmail)))

    def  get_email(self):
        return  WebDriverWait(self.driver,  60).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def  get_button_continue(self):
        return  WebDriverWait(self.driver,  60).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    def get_password(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_super(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.super)))

    def get_close_promo(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.close_promo)))


    """Actions"""

    def click_button_login_header(self):
        self.get_button_login_header().click()
        print("Click button 'Войти'")

    def click_button_gmail(self):
        self.get_button_gmail().click()
        print("Click button gmail")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click button continue")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_button_super(self):
        self.get_super().click()
        print("Click button super")

    def click_close_promo(self):
        self.get_close_promo().click()
        print("Click close_promo")



    """Methods"""

    def authorization_with_gmail(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.get_current_url()

        window_before = self.driver.window_handles[0]
        print(window_before)
        self.click_button_login_header()
        self.click_button_gmail()

        window_after = self.driver.window_handles[1]
        print(window_after)
        self.driver.switch_to.window(window_after)
        self.input_email("proflexia.test@gmail.com")
        self.click_button_continue()
        self.input_password("password_123456")
        self.click_button_continue()
        self.driver.switch_to.window(window_before)
        time.sleep(5)
        self.click_close_promo()
        print("\033[1m\033[32mSuccessful authorization! You can start shopping❤️\033[0m")








