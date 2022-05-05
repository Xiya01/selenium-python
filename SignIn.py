#Sign in page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from locators import *

class SignIn():

    def __init__(self, driver):
        self.driver = driver


    #1. Click "Sign in" button
    def click_sign_in(self):
        self.sign_in_a = self.driver.find_element(*SignInLocators.sign_in_btn).click()


    #2. Enter email
    def enter_mail(self, email):
        self.email_input = self.driver.find_element(*SignInLocators.email_btn)
        self.email_input.send_keys(email)


    #3. Click "create an account" button
    def click_create_account_button(self):
        self.create_account_btn = self.driver.find_element(*SignInLocators.account_btn).click()


    #4. Choose sex
    def choose_sex(self, sex):
        if sex == "F":
            # Choose Mrs
            self.driver.find_element(*SignInLocators.gender1).click()
        else:
            # Choose Mr
            self.driver.find_element(*SignInLocators.gender2).click()


    #5. Enter name
    def enter_firstname(self, name):
        first_name_input = self.driver.find_element(*SignInLocators.name_btn)
        first_name_input.send_keys(name)


    #6. Enter last name
    def enter_lastname(self, surname):
        last_name_input = self.driver.find_element(*SignInLocators.lastname_btn)
        last_name_input.send_keys(surname)


    #7. Enter password
    def enter_password(self, password):
        email_input = self.driver.find_element(*SignInLocators.pasd_btn)
        email_input.send_keys(password)


    #8. Enter date of birth
    def select_datebirth(self, birthdate):
        birthday_l = birthdate.split("-")
        birthday = str(int(birthday_l[2]))
        birthmonth = str(int(birthday_l[1]))
        birthyear = birthday_l[0]
        days_s = Select(self.driver.find_element(*SignInLocators.day_btn))
        days_s.select_by_value(birthday)
        months_s = Select(self.driver.find_element(*SignInLocators.month_btn))
        months_s.select_by_value(str(int(birthmonth)))
        years_s = Select(self.driver.find_element(*SignInLocators.year_btn))
        years_s.select_by_value(birthyear)


    #9. Enter address
    def enter_address(self, address):
        address_input = self.driver.find_element(*SignInLocators.address_btn)
        address_input.send_keys(address)


    #10. Enter city
    def enter_city(self, city):
        city_input = self.driver.find_element(*SignInLocators.city_btn)
        city_input.send_keys(city)


    #11. Select state
    def select_state(self, state_no):
        state_sel = Select(self.driver.find_element(*SignInLocators.state_btn))
        state_sel.select_by_value(state_no)

    #12. Enter postcode
    def enter_zip(self, zip_code):
        zip_input = self.driver.find_element(*SignInLocators.postcode_btn)
        zip_input.send_keys(zip_code)


    #13. Select country
    def select_country(self, country):
        country_input = self.driver.find_element(*SignInLocators.country_btn)
        country_input.send_keys(country)


    #14.Enter mobile phone number
    def enter_mobile_phone(self, phone):
        phone_input = self.driver.find_element(*SignInLocators.phone_btn)
        phone_input.send_keys(phone)


    #14. Assign an address alias for future reference
    def enter_assign_address(self, asign):
        assign_input = self.driver.find_element(*SignInLocators.alias_btn).clear()
        assign_input = self.driver.find_element(*SignInLocators.alias_btn).send_keys(asign)


    #15. Click button register
    def click_register_button(self):
        self.register_button = self.driver.find_element(*SignInLocators.submit_btn).click()


    #16. Click Sign out
    def click_sign_out(self):
        self.sign_out_button = self.driver.find_element(*SignInLocators.sign_out_btn).click()
