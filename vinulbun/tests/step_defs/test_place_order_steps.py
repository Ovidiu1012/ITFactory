from time import sleep
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.Locators import SearchpageLocators
from Locators.Locators import CartpageLocators
from Locators.Locators import OrderpageLocators
from Pages.Home_page import Homepage
from Pages.Login_page import Loginpage
from Pages.Search_page import Searchpage
from Pages.Item_page import Itempage
from Pages.Cart_page import Cartpage
from Pages.Order_page import Orderpage

scenarios('../features/add_order.feature')

@given('Open HomePage')
def open_homepage(browser):
    Homepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")
@when("Login")
def login(browser):
    Homepage(browser).open_login()
    Loginpage(browser).type_username()
    Loginpage(browser).type_password()
    Loginpage(browser).click_login()
    print("\n---Step 2---When---Pass---")
@when("Search item")
def search(browser):
    Homepage(browser).load_page()
    Homepage(browser).input_variables()
    Homepage(browser).click_search()
    print("\n---Step 3---When---Pass---")
@when("Add to cart")
def add_cart(browser):
    Searchpage(browser).add_to_cart()
    print("\n---Step 4---When---Pass---")
@then('Order registered')
def place_order(browser):
    sleep(3)
    WebDriverWait(browser, 15).until_not(EC.visibility_of_element_located((SearchpageLocators.notification_add)))
    sleep(5)
    Searchpage(browser).open_cart()
    sleep(5)
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((CartpageLocators.cookies)))
    Cartpage(browser).cookies()
    Cartpage(browser).confirm_order()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((OrderpageLocators.delivery_mode)))
    Orderpage(browser).delivery()
    WebDriverWait(browser, 5).until_not(EC.visibility_of_element_located((OrderpageLocators.notify_delivery)))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((OrderpageLocators.payment_mode)))
    Orderpage(browser).payment()
    WebDriverWait(browser, 5).until_not(EC.visibility_of_element_located((OrderpageLocators.notify_payment)))
    Orderpage(browser).details()
    #sleep(5)
    Orderpage(browser).terms_conditions()
    Orderpage(browser).place_order()
    print("\n---Step 5---Then---Pass---")


