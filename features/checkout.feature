@logging
@capture
Feature: Ecommerce Checkout

    Scenario: Find and click "add to cart" button
        Given url of product page to check add to cart
        When add to cart found
        Then click on add to cart and proceed to next step

    @skip_checkout_step_1
    Scenario: Find "cart/checkout" button
        Given In page, product is added into cart
        When cart/check out button found
        Then Click to proceed

    @skip_checkout_step_2
    Scenario: Find "Checkout/Proceed to checkout" button
        Given product detailed page
        When checkout or proceed to checkout button found
        Then click to move further
