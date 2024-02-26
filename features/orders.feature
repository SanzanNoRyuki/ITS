# -- AUTHOR: Roman Fulla <xfulla00>
Feature: Order History

  Scenario: Add order to history
    Given the customer is logged in his account
     When the customer places an order
     Then Order History contains this order

  Scenario: Check order information
    Given the logged customer has placed an order
     When the customer clicks on the "View" next to order
     Then the order information is displayed
