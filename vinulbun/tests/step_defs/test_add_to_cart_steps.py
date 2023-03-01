from time import sleep
from pytest_bdd import scenario, given, when, then, scenarios
from Pages.Home_page import Homepage
from Pages.Search_page import Searchpage
from Pages.Item_page import Itempage

scenarios('../features/add_to_cart.feature')

@given('Open Homepage')
def open_homepage(browser):
    Homepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")
@when('Search a given item')
def search(browser):
    Homepage(browser).input_variables()
    Homepage(browser).click_search()
    print("\n---Step 2---When---Pass---")
@when("Adding to cart the item")
def add_result(browser):
    Searchpage(browser).select_first_result()
    Itempage(browser).add_to_cart()
    print("\n---Step 3---When---Pass---")
@then('Verify if the item is added into the cart')
def verify(browser):
    expected = 1
    sleep(5)
    #WebDriverWait(browser,5).until(EC.presence_of_element_located((ItempageLocators.notification_add)))
    assert Itempage(browser).cart_info() == expected, "The item has not been successfully added to the cart!"
    print("\n---Step 4---Then---Pass---")
