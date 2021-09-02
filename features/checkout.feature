@logging
@capture
Feature: Ecommerce Checkout

    Scenario: Find and click buy now button
        Given url of product page
        When buy now found
        Then click on buy now and proceed to next step
#
#    @skip_add_to_cart
#    Scenario: Find and click "add to cart" button
#        Given url of product page to check add to cart
#        When add to cart found
#        Then click on add to cart and proceed to next step
#
#    @skip_checkout_step_1
#    Scenario: Find "cart/checkout" button
#        Given In page, product is added into cart
#        When cart/check out button found
#        Then Click to proceed
#
#    @skip_checkout_step_2
#    Scenario: Find "Checkout/Proceed to checkout" button
#        Given product detailed page
#        When checkout or proceed to checkout button found
#        Then click to move further

    Scenario: Perform login as guest
        Given Is product page has "login as guest" feature
        When product page support "login as guest" feature
        Then we should perform "login as guest"

    @skip_personal_info
    Scenario: Fill personal information
        Given information required page
        When personal information is required
        Then fill the information and proceed to next step

    @skip_login
    Scenario: Perform login with credentials
        Given Is "login" required
        Then perform "login" with credentials

    Scenario: Identify shipping page type and enter shipping details and proceed
        Given Shipping information required page
        When Shipping information found or not
        Then Enter shipping address details and proceed
