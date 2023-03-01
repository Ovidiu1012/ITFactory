Feature: Empty cart
  As a visitor of the page,
  I want to find a product,
  Add it to the cart,
  Empty the cart

  Scenario: Empty cart
    Given Open Homepage
    When Search a given item
    And Adding the first item found to cart
    And Empty the cart
    Then Verify if the cart is empty