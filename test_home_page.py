from selenium import webdriver
import unittest

#Quick homepage test
class HomePage(unittest.TestCase):

    def setUp(self):
        #Preparing test
        #Preconditions
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_home_page(self):
        self.driver.get("http://automationpractice.com/")
        self.driver.refresh()
        get_title = self.driver.title
        self.assertEqual("My Store", get_title)


    def tearDown(self):
        self.driver.quit()
        print("Done")

if __name__ == "__main__":
    unittest.main(verbosity=2)
