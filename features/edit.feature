# -- AUTHOR: Roman Fulla <xfulla00>
Feature: Edit Account

  Scenario: Edit Account access
    Given the logged customer is at the My Account page
     When the customer clicks on the "Edit Account"
     Then the customer is taken to his edit page

  Scenario: Change of e-mail adress
    Given the customer is at his edit page
     When the customer enters new "E-mail"
     And  the customer clicks on the "Continue"
     Then the customer "E-mail" is changed

  Scenario: Login into an account with an old e-mail
    Given the customer has edited his "E-mail"
     When the customer tries to login with an "Old E-mail"
     Then the customer access is denied
