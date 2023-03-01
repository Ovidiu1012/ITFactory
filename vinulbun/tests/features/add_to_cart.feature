Feature: Add to cart an item
  As a visitor of the page,
  I want to find a product,
  Add it to the cart

  Scenario: Add an item to cart
    Given Open Homepage
    When Search a given item
    When Adding to cart the item
    Then Verify if the item is added into the cart