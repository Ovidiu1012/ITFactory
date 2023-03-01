from Locators.Locators import ItempageLocators

class Itempage:
    def __init__(self,browser):
        self.browser = browser

    def add_to_cart(self):
        self.browser.find_element(*ItempageLocators.add_to_cart_button).click()

    def cart_info(self):
        qty = int(self.browser.find_element(*ItempageLocators.cart_qty).text)
        return qty
