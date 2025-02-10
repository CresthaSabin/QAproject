import time
import unittest



from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.Login import Signin
from Pages.Addtocart import Addtocart
from Pages.checkout import Checkout


class Test(unittest.TestCase):


   def setUp(self):

       self.driver = webdriver.Edge()
       self.driver.maximize_window()
       self.driver.get("https://gb.bishalkarki.com/index.php")

   def test_CheckoutGB(self):
        driver = self.driver
        self.lp = Signin(driver)
        self.atc=Addtocart(driver)
        self.ck= Checkout(driver)
        self.lp.SigninPage()
        self.lp.credential("yovoh22831@intady.com","Testing123")
        time.sleep(3)
        self.lp.login()
        time.sleep(3)
        self.atc.yourLoga()
        self.atc.image1()
        self.atc.addtocart1()
        self.atc.contshoppng()
        self.atc.yourLoga()
        self.atc.popular()
        self.atc.image2()
        self.atc.addtocart()
        self.ck.checkout1()
        self.ck.checkout2()
        self.ck.checkout3()
        self.ck.checkbox()
        self.ck.checkout4()
        self.ck.pay_by_bank()
        self.ck.confirm_my_order()





   def tearDown(self):
       self.driver.close()


