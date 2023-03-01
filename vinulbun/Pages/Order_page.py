from Locators.Locators import OrderpageLocators
from Utils.Variables import Details

class Orderpage:
    def __init__(self,browser):
        self.browser = browser

    def delivery(self):
        self.browser.find_element(*OrderpageLocators.delivery_mode).click()

    def payment(self):
        self.browser.find_element(*OrderpageLocators.payment_mode).click()

    def details(self):
        self.browser.find_element(*OrderpageLocators.details).send_keys(Details.obs)

    def terms_conditions(self):
        self.browser.find_element(*OrderpageLocators.terms).click()

    def place_order(self):
        self.browser.find_element(*OrderpageLocators.place_order).click()