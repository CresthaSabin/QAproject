import time
import unittest



from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.Login import Signin
from Pages.Addtocart import Addtocart


class Test(unittest.TestCase):


   def setUp(self):

       self.driver = webdriver.Edge()
       self.driver.maximize_window()
       self.driver.get("https://gb.bishalkarki.com/index.php")

   def test_AddtocartGB(self):
        driver = self.driver
        self.lp = Signin(driver)
        self.atc=Addtocart(driver)
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





   def tearDown(self):
       self.driver.close()


