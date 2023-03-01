Feature: Check if i can Login
  As a visitor of the page,
  I want to introduce user and password,
  So i can login

  Scenario: Login successfully
    Given Open LoginPage
    When Insert user
    When Insert password
    When Click Login button
    Then Login succesfully
