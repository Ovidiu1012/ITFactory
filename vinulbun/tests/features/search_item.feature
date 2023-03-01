Feature: Check if an item is available
  As a visitor of the page,
  I want to find an item

  Scenario: Find item
    Given Open Homepage
    When Input a given item in search
    And Search for results
    Then Find if the item is available