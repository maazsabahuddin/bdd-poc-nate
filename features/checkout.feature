@logging
@capture
Feature: Ecommerce Checkout

    Scenario: Find and click buy now button
        Given url of product page
        When buy now found
        Then click on buy now and proceed to next step

    @skip_add_to_cart
    Scenario: Find and click "add to cart" button
        Given url of product page to check add to cart
        When add to cart found
        Then click on add to cart and proceed to next step

    @skip_checkout_step_1
    Scenario: Find "cart/checkout" button
        Given In page, product is added into cart
        When cart/check out button found
        Then Click to proceed

   
