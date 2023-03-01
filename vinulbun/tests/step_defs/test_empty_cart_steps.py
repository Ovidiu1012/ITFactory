from time import sleep
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.Locators import SearchpageLocators
from Locators.Locators import ItempageLocators
from Locators.Locators import CartpageLocators
from Pages.Home_page import Homepage
from Pages.Search_page import Searchpage
from Pages.Item_page import Itempage
from Pages.Cart_page import Cartpage

scenarios('../features/empty_cart.feature')

@given('Open Homepage')
def open_homepage(browser):
    Homepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")
@when('Search a given item')
def search(browser):
    Homepage(browser).input_variables()
    Homepage(browser).click_search()
    print("\n---Step 2---When---Pass---")
@when("Adding the first item found to cart")
def add_item(browser):
    Searchpage(browser).add_to_cart()
    WebDriverWait(browser, 15).until_not(EC.visibility_of_element_located((SearchpageLocators.notification_add)))
    print("\n---Step 3---When---Pass---")
@when("Empty the cart")
def empty(browser):
    Searchpage(browser).open_cart()
    Cartpage(browser).empty()
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((CartpageLocators.confirm_empty)))
    Cartpage(browser).confirm()
    print("\n---Step 4---When---Pass---")
@then('Verify if the cart is empty')
def verify(browser):
    expected = 'Nu sunt produse adăugate în coș!'
    sleep(1)
    assert Cartpage(browser).warning_cart() == expected, 'Cosul nu a fost golit!'
    print("\n---Step 5---Then---Pass---")
