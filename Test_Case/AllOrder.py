import time
import unittest
from selenium import webdriver

from Pages.AllOrder import Orders
from Pages.Login import Signin


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://gb.bishalkarki.com/index.php")

    def test_loginGB(self):
        driver = self.driver
        self.lp = Signin(driver)
        self.ord = Orders(driver)
        self.lp.SigninPage()
        self.lp.credential("yovoh22831@intady.com", "Testing123")
        time.sleep(3)
        self.lp.login()
        time.sleep(3)
        self.ord.Order()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()