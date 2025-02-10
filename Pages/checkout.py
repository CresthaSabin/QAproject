import time

from selenium.webdriver.common.by import By

from Locator.Locator import Locate

class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locate()

    #checkout
    def checkout1(self):
        driver = self.driver
        lc = self.lc
        checkout_button1= driver.find_element(By.XPATH,lc.checkout_button1_xpath)
        checkout_button1.click()

    def checkout2(self):
        driver = self.driver
        lc = self.lc
        checkout_button2 = driver.find_element(By.XPATH, lc.checkout_button2_xpath)
        checkout_button2.click()

    def checkout3(self):
        driver = self.driver
        lc = self.lc
        checkout_button3 = driver.find_element(By.XPATH, lc.checkout_button3_xpath)
        checkout_button3.click()

    def checkbox(self):
        driver = self.driver
        lc = self.lc
        check_box = driver.find_element(By.XPATH,lc.check_box_xpath)
        check_box.click()


    def checkout4(self):
        driver = self.driver
        lc = self.lc
        checkout_button4 = driver.find_element(By.XPATH, lc.checkout_button4_xpath)
        checkout_button4.click()

    def pay_by_bank(self):
        driver = self.driver
        lc = self.lc
        pay_by_bank = driver.find_element(By.XPATH, lc.pay_by_bank_xpath)
        pay_by_bank.click()

    def  confirm_my_order(self):
        driver = self.driver
        lc = self.lc
        confirm_my_order = driver.find_element(By.XPATH, lc.confirm_my_order_xpath)
        confirm_my_order.click()