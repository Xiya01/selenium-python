from selenium import webdriver
import unittest
import time
from LogIn import LogIn
from SignIn import SignIn
from faker import Faker
from BaseTest import BaseTest
from test_sign_in import signInTestTemplate
from selenium.webdriver.common.by import By

#Test data
invalid_email = "@com.pl" #mail nie zgadza sie z podanym pzy rejestracji
empty_email = "" #empty space
invalid_password = "1" #haslo inne niz podane przy rejestracji,
empty_password = "" #empty space


def login_template(driver, email, password):
    login = LogIn(driver)
    login.click_sign_in()
    login.enter_login_email(email)
    login.enter_login_password(password)
    login.click_log_in()


class LogInTest(BaseTest):

    def test_valid1(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, valid_email, valid_password)
        compliance_inf = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign out")
        self.assertEqual("Sign out", compliance_inf.get_attribute("innerText"))

        time.sleep(5)


    def test_invalid_mail(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, invalid_email, valid_password)
        compliance_inf = self.driver.find_element(By.ID, "email")
        self.assertEqual(invalid_email, compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_empty_mail(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, empty_email, valid_password)
        compliance_inf = self.driver.find_element(By.ID, "email")
        self.assertEqual(empty_email, compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_invalid_password(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, valid_email, invalid_password)
        compliance_inf = self.driver.find_element(By.ID, "passwd")
        self.assertEqual(invalid_password, compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_empty_password(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, valid_email, empty_password)
        compliance_inf = self.driver.find_element(By.ID, "passwd")
        self.assertEqual(empty_password, compliance_inf.get_attribute("value"))

        time.sleep(5)



if __name__ == "__main__":
    unittest.main(verbosity=2)
