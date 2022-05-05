
from selenium import webdriver
import unittest
import time


class BaseTest(unittest.TestCase):

    def setUp(self):
        #Preparing test
        #Preconditions
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")


    def tearDown(self):
        self.driver.quit()
        print("Done")

if __name__ == "__main__":
    unittest.main(verbosity=2)
