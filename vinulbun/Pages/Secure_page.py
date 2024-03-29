from Locators.Locators import SecurepageLocators

class Securepage:
    def __init__(self,browser):
        self.browser = browser
    def load_page(self):
        self.browser.get(SecurepageLocators.URL)
        sleep(3)
    def get_message(self):
        return self.browser.find_element(*SecurepageLocators.success_msg).text
    def click_logout(self):
        self.browser.find_element(*SecurepageLocators.logout_btn).click()
    def verify_login(self):
        v = self.browser.find_element(*SecurepageLocators.verify).is_displayed()
        return v