@logging
@capture
Feature: Ecommerce Checkout

#    Scenario: Find and click buy now button
#        Given url of product page
#        When buy now found
#        Then click on buy now and proceed to next step
#
#    @skip_add_to_cart
#    Scenario: Find and click "add to cart" button
#        Given url of product page to check add to cart
#        When add to cart found
#        Then click on add to cart and proceed to next step
#
#    Scenario: Perform login as guest
#        Given Is product page has "login as guest" feature
#        When product page support "login as guest" feature
#        Then we should perform "login as guest"
#
#    @skip_login
#    Scenario: Perform login with credentials
#        Given Is "login" required
#        Then perform "login" with credentials


    Scenario: Identify shipping page type and enter shipping details and proceed
        Given Find type of shipping address page
        When Shipping page ask about shipping address details
        Then Enter shipping address details and proceed
