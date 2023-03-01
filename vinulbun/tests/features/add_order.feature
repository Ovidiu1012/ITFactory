Feature: Add order
  As a visitor of the page,
  I want to login,
  Search an item,
  Add to cart,
  Place the order

  Scenario: Add order
    Given Open HomePage
    When Login
    When Search item
    When Add to cart
    Then Order registered
