import time
import unittest



from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.Login import Signin


class Test(unittest.TestCase):


   def setUp(self):

       self.driver = webdriver.Edge()
       self.driver.maximize_window()
       self.driver.get("https://gb.bishalkarki.com/index.php")

   def test_loginGB(self):
        driver = self.driver
        self.lp = Signin(driver)
        self.lp.SigninPage()
        self.lp.credential("neneray950@andinews.com","Test123")
        time.sleep(3)
        self.lp.login()
        time.sleep(3)

        expected_result = "Qa Project"
        actual_result= driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
        self.assertEqual(expected_result,actual_result,"Wrong info")

   def tearDown(self):
       self.driver.close()


