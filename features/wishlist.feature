# -- AUTHOR: Roman Fulla <xfulla00>
Feature: Wishlist

  Scenario: Access wishlist
    Given the customer has logged in
     When the customer clicks on the "Wish List"
     Then the customer is taken to his wishlist

  Scenario: Add featured product to wishlist
    Given the logged customer is at the store home page
     When the customer clicks on the "Canon EOS 5D"
     Then "Canon EOS 5D" is added to the customer wishlist

  Scenario: Remove product from wishlist
    Given the customer has "Canon EOS 5D" in his wishlist
     When the customer clicks on the "Remove" next to the "Canon EOS 5D"
     Then "Canon EOS 5D" is removed from the customer wishlist

  Scenario: Add product from wishlist to shopping cart
    Given the customer has "iPhone" in his wishlist
     When the customer clicks on the "Add to Cart" next to the "iPhone"
     Then "iPhone" is added to the customer shopping cart
