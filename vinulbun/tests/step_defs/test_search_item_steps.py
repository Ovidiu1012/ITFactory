from pytest_bdd import scenarios, given, when, then
from Locators.Locators import LoginpageLocators
from Locators.Locators import SearchpageLocators
from Pages.Home_page import Homepage
from Pages.Search_page import Searchpage

scenarios('../features/search_item.feature')

@given('Open Homepage')
def open_homepage(browser):
    Homepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")

@when('Input a given item in search')
def input(browser):
    Homepage(browser).input_variables()
    print("\n---Step 2---When---Pass---")
@when("Search for results")
def search(browser):
    Homepage(browser).click_search()
    print("\n---Step 3---When---Pass---")
@then('Find if the item is available')
def verify(browser):
    expected = True
    assert Searchpage(browser).results_search() == expected, "The item is not available!"
    print("\n---Step 4---Then---Pass---")

