@logging
@capture
Feature: Ecommerce Checkout

    Scenario: Find and click buy now button
        Given url of product page
        When buy now found
        Then click on buy now and proceed to next step

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