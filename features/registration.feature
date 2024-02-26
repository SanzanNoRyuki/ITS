# -- AUTHOR: Roman Fulla <xfulla00>
Feature: Registration process

  Scenario: Access My Account dropdown menu
    Given the customer is at the shop homepage
     When the customer clicks on the "My Account"
     Then My Account dropdown menu unfolds

  Scenario: Access Registration formular
    Given the customer isn't logged in
     When the customer clicks on the "Register"
     Then the customer is taken to the registration formular

  Scenario: Incomplete registration request
    Given the customer is at the registration formular page
     When the customer fills in every required field except the "City"
     Then registration is unsuccesful

  Scenario: Registration request with an incorrect value
    Given the customer is again at the registration formular page
     When the customer fills in every required field but the "Telephone" is misspelled
     Then registration isn't succesful

  Scenario: Succesful Registration
    Given the customer is once again at the registration formular page
     When the customer fills in every required field correctly
     Then registration is succesful

  Scenario: Registration with an already used e-mail
    Given the customer is at the registration formular page once more
     When the customer fills in every required field but the "E-mail" is already in use
     Then registration is not succesful
