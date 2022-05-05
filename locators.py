from selenium.webdriver.common.by import By


class SignInLocators(object):
    #A class for sign in page locators
    sign_in_btn = (By.PARTIAL_LINK_TEXT, "Sign in")
    email_btn = (By.ID, "email_create")
    account_btn = (By.ID, "SubmitCreate")
    gender1 = (By.ID, "id_gender1")
    gender2 = (By.ID, "id_gender2")
    name_btn = (By.ID, "customer_firstname")
    lastname_btn = (By.ID, "customer_lastname")
    pasd_btn = (By.ID, "passwd")
    day_btn = (By.ID, "days")
    month_btn = (By.ID, "months")
    year_btn = (By.ID, "years")
    address_btn = (By.ID, "address1")
    city_btn = (By.ID, "city")
    state_btn = (By.ID, "id_state")
    postcode_btn = (By.ID, "postcode")
    country_btn = (By.ID, "id_country")
    phone_btn = (By.ID, "phone_mobile")
    alias_btn = (By.ID, "alias")
    submit_btn = (By.ID, "submitAccount")
    sign_out_btn = (By.PARTIAL_LINK_TEXT, "Sign out")



class LogInLocators(object):
    #A class for log in page locators
    sign_in_btn = (By.PARTIAL_LINK_TEXT, "Sign in")
    mail_btn = (By.ID, "email")
    passy = (By.ID, "passwd")
    submit_btn = (By.ID, "SubmitLogin")



class ShoppingLocators(object):
    #A class for shopping page locators
    women_btn = (By.PARTIAL_LINK_TEXT, "WOMEN")
    tshirt_btn = (By.PARTIAL_LINK_TEXT, "Faded Short Sleeve T-shirts")
    quality_btn = (By.ID, "quantity_wanted")
    size_btn = (By.ID, "group_1")
    color_btn = (By.ID, "color_13")
    add_btn = (By.ID, "add_to_cart")
    checkout_btn = (By.PARTIAL_LINK_TEXT, "Proceed to checkout")
    checkout1 = (By.PARTIAL_LINK_TEXT, "Proceed to checkout")
    checkout2 = (By.XPATH, '(//div/form/p/button[@class="button btn btn-default button-medium"])')
    terms_btn = (By.ID, "cgv")
    checkout3 = (By.XPATH, '(//div/form/p/button[@class="button btn btn-default standard-checkout button-medium"])')
    payment_btn = (By.PARTIAL_LINK_TEXT, "Pay by bank wire")
    confirm_btn = (By.XPATH, '(//div/form/p/button[@class="button btn btn-default button-medium"])')
