from pytest_bdd import scenarios, given, when, then
from Locators.Locators import LoginpageLocators
from Pages.Home_page import Homepage


scenarios('../features/form_authentification.feature')

@given('Open Homepage')
def open_homepage(browser):
    Homepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")
@when("Find Form Authentification and click on it")
def open_login(browser):
    Homepage(browser).open_login()
    print("\n---Step 2---When---Pass---")
@then('Redirect to Loginpage')
def login(browser):
    assert browser.current_url == LoginpageLocators.URL, "Main page URL is not ok."
    print("\n---Step 3---Then---Pass---")

