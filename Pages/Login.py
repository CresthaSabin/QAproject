import time

from Locator.Locator import Locate

from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
         self.driver = driver
         self.lc = Locate()



    def SigninPage(self,username,password):
        driver = self.driver
        lc = self.lc

        #Click Sign in
        sign_in = driver.find_element(By.XPATH,lc.signin_xpath)
        sign_in.click()

        #Enter Username
        driver.implicitly_wait(10)
        user_name = driver.find_element(By.ID,lc.username_id)
        user_name.send_keys(username)

        #Enter password
        pwd_word = driver.find_element(By.ID,lc.pswd_id)
        pwd_word.send_keys(password)

        #Click sign in button
        signin_btn = driver.find_element(By.XPATH,lc.signin_btn_xpath)
        signin_btn.click()
        time.sleep(10)



