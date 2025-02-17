import unittest
from selenium import webdriver

from Pages.SignOut import Signout


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://gb.bishalkarki.com/index.php")

    def test_SignoutGB(self):
        driver=self.driver
        self.so = Signout(driver)
        self.so.signinPage()
        self.so.credential("yovoh22831@intady.com","Testing123")
        self.so.login()
        self.so.yourLoga()
        self.so.signout()

    def tearDown(self):
        self.driver.close()




if __name__ == '__main__':
    unittest.main()
