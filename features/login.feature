# -- AUTHOR: Roman Fulla <xfulla00>
Feature: Login & Logout process

  Scenario: Access login page
    Given the customer is at the store homepage
     When the customer clicks on the "Login"
     Then the customer is taken to the login page

  Scenario: Wrong login informations
    Given the customer is at the login page
     When the customer fills in incorrect informations
     Then the customer has denied access

  Scenario: Login into an account
    Given the customer already has an account
     When the customer fills in correct informations
     Then the customer is successfully logged in

  Scenario: Logout from an account
    Given the customer is logged in
     When the customer clicks on the "Logout"
     Then the customer is logged out
