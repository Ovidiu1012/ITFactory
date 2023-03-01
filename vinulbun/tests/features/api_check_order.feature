Feature: Check order in DB
  After placing an order in OrderPage,
  With credentials provided for endpoint
  Check if the order is registered in DB

  Scenario: Check order in DB
    Given Open Connection
    When Set params
    Then Check if the order is registered
