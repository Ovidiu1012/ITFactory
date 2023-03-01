from Locators.Locators import CartpageLocators

class Cartpage:
    def __init__(self,browser):
        self.browser = browser

    def empty(self):
        self.browser.find_element(*CartpageLocators.empty_cart).click()

    def confirm(self):
        self.browser.find_element(*CartpageLocators.confirm_empty).click()

    def confirm_order(self):
        self.browser.find_element(*CartpageLocators.order).click()

    def cookies(self):
        self.browser.find_element(*CartpageLocators.cookies).click()

    def warning_cart(self):
       actual = self.browser.find_element(*CartpageLocators.warning).text
       return actual