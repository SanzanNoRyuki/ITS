# -- AUTHOR: Roman Fulla <xfulla00>
Feature: Adress autofill

  Scenario: Autofill of billing details
    Given the logged customer is at the checkout
     When the customer wants to use an existing address
     Then "Billing Details" are automatically filled in
