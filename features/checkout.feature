@logging
@capture
Feature: Ecommerce Checkout

    Scenario: Find and click "add to cart" button
        Given url of product page to check add to cart
        When add to cart found
        Then click on add to cart and proceed to next step

    Scenario: Find "cart/checkout" button
        Given In page, product is added into cart
        When cart/check out button found
        Then Click to proceed

    @skip_checkout_step_2
    Scenario: Find "Checkout/Proceed to checkout" button
        Given product detailed page
        When checkout or proceed to checkout button found
        Then click to move further

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

    Scenario: Find payment flow and proceed
        Given Payment Button
        When If payment button found
        Then Click on it

    Scenario: Fill card details
        Given order card details page
        When card details found
        Then fill the details and proceed to next step

    Scenario: Review order
        Given order page
        When review order button found
        Then review order and proceed to next step

    Scenario: Confirm and Pay
        Given order confirmation page
        When confirm and pay found and interactable
        Then confirm order and pay
