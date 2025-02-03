import time

from Locator.Locator import Locate

from selenium.webdriver.common.by import By


class Signin:
    def __init__(self,driver):
         self.driver = driver
         self.lc = Locate()



    def SigninPage(self):
        driver = self.driver
        lc = self.lc

        #Click Sign in
        sign_in = driver.find_element(By.XPATH,lc.nav_signin_xpath)
        sign_in.click()

    def credential(self, username, password):
        #Enter Username
        self.driver.implicitly_wait(10)
        user_name = self.driver.find_element(By.ID,self.lc.email_field_id)
        user_name.send_keys(username)

        #Enter password
        pwd_word = self.driver.find_element(By.ID,self.lc.password_field_id)
        pwd_word.send_keys(password)

    def login(self):
        #Click sign in button
        signin_btn = self.driver.find_element(By.XPATH,self.lc.login_btn_xpath)
        signin_btn.click()
        time.sleep(10)



