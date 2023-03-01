from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pytest_bdd import scenario, given, when, then, scenarios
from Locators.Locators import SecurepageLocators
from Pages.Login_page import Loginpage
from Pages.Secure_page import Securepage

scenarios('../features/login_page.feature')

@given('Open LoginPage')
def load_page(browser):
    Loginpage(browser).load_page()
    print("\n---Step 1---Given---Pass---")
@when("Insert user")
def type_user(browser):
    Loginpage(browser).type_username()
    print("\n---Step 2---When---Pass---")
@when("Insert password")
def type_pass(browser):
    Loginpage(browser).type_password()
    print("\n---Step 3---When---Pass---")
@when("Click Login button")
def click_login(browser):
    Loginpage(browser).click_login()
    print("\n---Step 4---When---Pass---")
@then ('Login succesfully')
def verify(browser):
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((SecurepageLocators.verify2)))
    assert browser.current_url == SecurepageLocators.URL and Securepage(browser).verify_login() == True, "Login not successfully!"
    print("\n---Step 5---Then---Pass---")
