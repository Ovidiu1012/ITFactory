from Locators.Locators import HomepageLocators
from Utils.Variables import Variables
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self,browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(HomepageLocators.URL)
        if self.browser.find_element(*HomepageLocators.age_verify).is_displayed() == True:
            self.browser.find_element(*HomepageLocators.age_verify_true).click()

    def click_search(self):
        self.browser.find_element(*HomepageLocators.search_button).click()

    def click_home(self):
        self.browser.find_element(*HomepageLocators.home_button).click()

    def input_variables(self):
        self.browser.find_element(*HomepageLocators.search).send_keys(Variables.search_item)

    def open_login(self):
        self.browser.find_element(*HomepageLocators.login).click()




