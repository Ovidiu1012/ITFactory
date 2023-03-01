from Locators.Locators import LoginpageLocators
from Locators.Locators import HomepageLocators
from Utils.Variables import Credentials

class Loginpage:
    def __init__(self,browser):
        self.browser = browser
    def load_page(self):
        self.browser.get(LoginpageLocators.URL)
        if self.browser.find_element(*HomepageLocators.age_verify).is_displayed() == True:
            self.browser.find_element(*HomepageLocators.age_verify_true).click()
    def type_username(self):
        self.browser.find_element(*LoginpageLocators.user).send_keys(Credentials.email)
    def type_password(self):
        self.browser.find_element(*LoginpageLocators.password).send_keys(Credentials.pwd)
    def click_login(self):
        self.browser.find_element(*LoginpageLocators.login_btn).click()