#Quick login page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from locators import *

#Quick login test
class LogIn():

    def __init__(self, driver):
        self.driver = driver

#1. Click sign in button
    def click_sign_in(self):
        self.sign_in_a = self.driver.find_element(*LogInLocators.sign_in_btn).click()

#2. Write e-mail
    def enter_login_email(self, logmail):
        login_email_input= self.driver.find_element(*LogInLocators.mail_btn)
        login_email_input.send_keys(logmail)

#3. Write password
    def enter_login_password(self, logpass):
        log_in_password_input= self.driver.find_element(*LogInLocators.passy)
        log_in_password_input.send_keys(logpass)


#4. Click login button
    def click_log_in(self):
        log_in_button = self.driver.find_element(*LogInLocators.submit_btn).click()
