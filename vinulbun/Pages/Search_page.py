from Locators.Locators import SearchpageLocators

class Searchpage:
    def __init__(self,browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(HomepageLocators.URL)
        if self.browser.find_element(*HomepageLocators.age_verify).is_displayed() == True:
            self.browser.find_element(*HomepageLocators.age_verify_true).click()

    def results_search(self):
        actual = self.browser.find_element(*SearchpageLocators.item_results).is_displayed()
        return actual

    def select_first_result(self):
        self.browser.find_element(*SearchpageLocators.item_results).click()

    def add_to_cart(self):
        self.browser.find_element(*SearchpageLocators.add_to_cart_button).click()

    def open_cart(self):
        self.browser.find_element(*SearchpageLocators.cart).click()