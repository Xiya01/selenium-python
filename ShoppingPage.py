#Shopping page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from locators import *
from selenium.webdriver.support import expected_conditions as EC

#Quick shopping test
class ShoppingPage():

    def __init__(self, driver):
        self.driver = driver

    #1. Choose "women" button
    def click_women_button(self):
        women_dress = self.driver.find_element(*ShoppingLocators.women_btn).click()

    #2. Choose product
    def click_product(self):
        tshirt_button = self.driver.find_element(*ShoppingLocators.tshirt_btn).click()

    #3. Enter Quantity
    def enter_quantity(self, quantity):
        quantity_input = self.driver.find_element(*ShoppingLocators.quality_btn).clear()
        quantity_input = self.driver.find_element(*ShoppingLocators.quality_btn).send_keys(quantity)

    #4. Choose size
    def select_size(self, size):
        select_size = Select(self.driver.find_element(*ShoppingLocators.size_btn))
        select_size.select_by_value(size)

    #5 Choose color
    def choose_color(self):
        color_pick = self.driver.find_element(*ShoppingLocators.color_btn).click()

    #6. Add product to cart
    def click_add_to_cart(self):
        add_to_cart_button = self.driver.find_element(*ShoppingLocators.add_btn).click()


    #7. Comfirm the purchase
    def checkout_button(self):
        checkout_button = self.driver.find_element(*ShoppingLocators.checkout_btn).click()

    #8. Click proceed to checkout
    def proceed_to_checkout_button1(self):
        proceed_to_checkout_button1 = self.driver.find_element(*ShoppingLocators.checkout1).click()

    #8. Click proceed to checkout
    def proceed_to_checkout_button2(self):
        proceed_to_checkout_button2 = self.driver.find_element(*ShoppingLocators.checkout2).click()

    #9. Agree to the terms of service
    def agree_terms_window(self):
        click_agree_terms = self.driver.find_element(*ShoppingLocators.terms_btn).click()


    #10. Click proceed to checkout
    def proceed_to_checkout_button3(self):
        click_proceed_to_checkout3 = self.driver.find_element(*ShoppingLocators.checkout3).click()


    #11. Choose way of payment
    def click_payment_button(self):
        pay_by_bank_wire_button= self.driver.find_element(*ShoppingLocators.payment_btn).click()


    #12. Click confirm order
    def click_confrim_order(self):
        confirm_order_button= self.driver.find_element(*ShoppingLocators.confirm_btn).click()
