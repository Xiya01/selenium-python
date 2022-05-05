from selenium import webdriver
import unittest
import time
from SignIn import SignIn
from faker import Faker
from BaseTest import BaseTest
from selenium.webdriver.common.by import By



fake = Faker("en_US")
#Test data
sex_c = fake.random_element(elements=("M","F"))
state = str(fake.random_int(min=1, max=50))
valid_email = fake.email()
valid_name = fake.name()
valid_surname = fake.last_name()
valid_password = fake.password(7)
valid_birthdate = fake.date()
valid_adress = fake.street_address()
valid_city = fake.city()
valid_postcode = fake.postcode()
valid_mobile_phone = fake.msisdn()
assign_address = "My address"
invalid_email = "@gm.com"
short_password = fake.password(4) # lenght < 5,
long_email = "tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeessssssstt@gm.com" #lenght > 128
empty_password = "" #empty place
long_password = fake.password(33) # lenght > 32



def signInTestTemplate(web_driver):

    fake = Faker("en_US")
    #Test data
    sex_c = fake.random_element(elements=("M","F"))
    state = str(fake.random_int(min=1, max=50))
    valid_email = fake.email()
    valid_name = fake.name()
    valid_surname = fake.last_name()
    valid_password = fake.password(7)
    valid_birthdate = fake.date()
    valid_adress = fake.street_address()
    valid_city = fake.city()
    valid_postcode = fake.postcode()
    valid_mobile_phone = fake.msisdn()
    assign_address = "My address"

    #homepage
    registration = SignIn(web_driver)
    registration.click_sign_in()
    #subpage - authentication
    registration.enter_mail(valid_email)
    registration.click_create_account_button()
    #subpage - registration
    registration.choose_sex(sex_c)
    registration.enter_firstname(valid_name)
    registration.enter_lastname(valid_surname)
    registration.enter_password(valid_password)
    registration.select_datebirth(valid_birthdate)
    registration.enter_address(valid_adress)
    registration.enter_city(valid_city)
    registration.select_state(state)
    registration.enter_zip(valid_postcode)
    registration.enter_mobile_phone(valid_mobile_phone)
    registration.enter_assign_address(assign_address)
    registration.click_register_button()
    registration.click_sign_out()

    time.sleep(5)

    return valid_email, valid_password


#Quick sign in test
class SignInTest(BaseTest):

    def test_valid(self):
        signInTestTemplate(self.driver)
        compliance_inf = self.driver.find_element(By.ID, "email_create")
        self.assertEqual("", compliance_inf.get_attribute("value"))


    def test_invalid_email(self):
        #homepage
        registration = SignIn(self.driver)
        registration.click_sign_in()
        #subpage - authentication
        registration.enter_mail(invalid_email)
        registration.click_create_account_button()
        time.sleep(3)
        compliance_inf = self.driver.find_element(By.ID, "email_create")
        self.assertEqual(invalid_email, compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_empty_email(self):
        #homepage
        registration = SignIn(self.driver)
        registration.click_sign_in()
        #subpage - authentication
        registration.enter_mail("")
        registration.click_create_account_button()
        time.sleep(3)
        compliance_inf = self.driver.find_element(By.ID, "email_create")
        self.assertEqual("", compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_too_long_email(self):
        #homepage
        registration = SignIn(self.driver)
        registration.click_sign_in()
        #subpage - authentication
        registration.enter_mail(long_email)
        registration.click_create_account_button()
        #subpage - registration
        registration.choose_sex(sex_c)
        registration.enter_firstname(valid_name)
        registration.enter_lastname(valid_surname)
        registration.enter_password(valid_password)
        registration.select_datebirth(valid_birthdate)
        registration.enter_address(valid_adress)
        registration.enter_city(valid_city)
        registration.select_state(state)
        registration.enter_zip(valid_postcode)
        registration.enter_mobile_phone(valid_mobile_phone)
        registration.enter_assign_address(assign_address)
        registration.click_register_button()
        time.sleep(3)
        compliance_inf = self.driver.find_element(By.ID, "email")
        self.assertEqual(long_email, compliance_inf.get_attribute("value"))
        time.sleep(5)


    def test_too_short_password(self):
        #homepage
        registration = SignIn(self.driver)
        registration.click_sign_in()
        #subpage - authentication
        registration.enter_mail(valid_email)
        registration.click_create_account_button()
        #subpage - registration
        registration.choose_sex(sex_c)
        registration.enter_firstname(valid_name)
        registration.enter_lastname(valid_surname)
        registration.enter_password(short_password)
        registration.select_datebirth(valid_birthdate)
        registration.enter_address(valid_adress)
        registration.enter_city(valid_city)
        registration.select_state(state)
        registration.enter_zip(valid_postcode)
        registration.enter_mobile_phone(valid_mobile_phone)
        registration.enter_assign_address(assign_address)
        registration.click_register_button()
        time.sleep(3)
        compliance_inf = self.driver.find_element(By.ID, "passwd")
        self.assertEqual("", compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_empty_password(self):
        #homepage
        registration = SignIn(self.driver)
        registration.click_sign_in()
        #subpage - authentication
        registration.enter_mail(valid_email)
        registration.click_create_account_button()
        #subpage - registration
        registration.choose_sex(sex_c)
        registration.enter_firstname(valid_name)
        registration.enter_lastname(valid_surname)
        registration.enter_password(empty_password)
        registration.select_datebirth(valid_birthdate)
        registration.enter_address(valid_adress)
        registration.enter_city(valid_city)
        registration.select_state(state)
        registration.enter_zip(valid_postcode)
        registration.enter_mobile_phone(valid_mobile_phone)
        registration.enter_assign_address(assign_address)
        registration.click_register_button()
        time.sleep(3)
        compliance_inf = self.driver.find_element(By.ID, "passwd")
        self.assertEqual("", compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_too_long_password(self):
        #homepage
        registration = SignIn(self.driver)
        registration.click_sign_in()
        #subpage - authentication
        registration.enter_mail(valid_email)
        registration.click_create_account_button()
        #subpage - registration
        registration.choose_sex(sex_c)
        registration.enter_firstname(valid_name)
        registration.enter_lastname(valid_surname)
        registration.enter_password(long_password)
        registration.select_datebirth(valid_birthdate)
        registration.enter_address(valid_adress)
        registration.enter_city(valid_city)
        registration.select_state(state)
        registration.enter_zip(valid_postcode)
        registration.enter_mobile_phone(valid_mobile_phone)
        registration.enter_assign_address(assign_address)
        registration.click_register_button()
        time.sleep(3)
        compliance_inf = self.driver.find_element(By.ID, "passwd")
        self.assertEqual("", compliance_inf.get_attribute("value"))

        time.sleep(5)



if __name__ == "__main__":
    unittest.main(verbosity=2)
