import time

from selenium.webdriver.common.by import By

from Locator.Locator import Locate

class Addtocart:
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
    #Addto cart
    def yourLoga(self):
        driver = self.driver
        lc = self.lc
        #Click image
        yourLoga = driver.find_element(By.ID, lc.yourLoga_Logo_id )
        yourLoga.click()

    def image1(self):
        # image1
        self.driver.implicitly_wait(10)
        image1= self.driver.find_element(By.XPATH, self.lc.image1_xpath)
        image1.click()

    def addtocart1(self):
        #addtocart1
        self.driver.implicitly_wait(10)
        addcart1=self.driver.find_element(By.XPATH, self.lc.addtocart1_xpath)
        addcart1.click()

    def contshoppng(self):
        #contshoppng
        self.driver.implicitly_wait(10)
        contshoppng=self.driver.find_element(By.XPATH, self.lc.contshopping_xpath)
        contshoppng.click()

    def yourLoga(self):
            #Click image
        yourLoga = self.driver.find_element(By.ID, self.lc.yourLoga_Logo_id )
        yourLoga.click()

    def popular(self):
        #popular
        self.driver.implicitly_wait(10)
        popular=self.driver.find_element(By.XPATH, self.lc.popular_xpath)
        popular.click()

    def image2(self):
        # image2
        self.driver.implicitly_wait(10)
        image2= self.driver.find_element(By.XPATH, self.lc.image2_xpath)
        image2.click()
    def addtocart(self):
        #addtocart
        self.driver.implicitly_wait(10)
        addcart=self.driver.find_element(By.XPATH, self.lc.addtocart_xpath)
        addcart.click()

