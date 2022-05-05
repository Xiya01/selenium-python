from selenium import webdriver
import unittest
import time
from ShoppingPage import ShoppingPage
from faker import Faker
from BaseTest import BaseTest
from test_sign_in import signInTestTemplate
from test_log_in import login_template
from selenium.webdriver.common.by import By

fake = Faker("en_US")

#Test data
assign_address = "My address"
quantity = fake.random_int(min=1, max=100)
size = str(fake.random_int(min=1, max=3))
invalid_quantity = "0"


class ShoppingTest(BaseTest):

    def test_valid(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, valid_email, valid_password)
        shopping = ShoppingPage(self.driver)
        shopping.click_women_button()
        shopping.click_product()
        shopping.enter_quantity(quantity)
        shopping.select_size(size)
        shopping.choose_color()
        shopping.click_add_to_cart()
        shopping.checkout_button()
        shopping.proceed_to_checkout_button1()
        shopping.proceed_to_checkout_button2()
        shopping.agree_terms_window()
        shopping.proceed_to_checkout_button3()
        shopping.click_payment_button()
        shopping.click_confrim_order()
        compliance_inf = self.driver.find_element(By.ID, "step_end")
        self.assertEqual("05. Payment", compliance_inf.get_attribute("innerText"))

        time.sleep(5)


    def test_zero_quantity(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, valid_email, valid_password)
        shopping = ShoppingPage(self.driver)
        shopping.click_women_button()
        shopping.click_product()
        shopping.enter_quantity(invalid_quantity)
        shopping.select_size(size)
        shopping.choose_color()
        shopping.click_add_to_cart()
        compliance_inf = self.driver.find_element(By.ID, "quantity_wanted")
        self.assertEqual("0", compliance_inf.get_attribute("value"))

        time.sleep(5)


    def test_without_agree_terms(self):
        valid_email, valid_password = signInTestTemplate(self.driver)
        login_template(self.driver, valid_email, valid_password)
        shopping = ShoppingPage(self.driver)
        shopping.click_women_button()
        shopping.click_product()
        shopping.enter_quantity(quantity)
        shopping.select_size(size)
        shopping.choose_color()
        shopping.click_add_to_cart()
        shopping.checkout_button()
        shopping.proceed_to_checkout_button1()
        shopping.proceed_to_checkout_button2()
        shopping.proceed_to_checkout_button3()
        compliance_inf = self.driver.find_element(By.ID, "cgv")
        self.assertEqual("1", compliance_inf.get_attribute("value"))
        
        time.sleep(5)



if __name__ == "__main__":
    unittest.main(verbosity=2)
