Feature: Ecommerce Checkout

    Scenario: Find and click buy now button
        Given url of product page
        When buy now button found skip add to cart
        Then we should land to login page
    
    @skip_add_to_cart
    Scenario: Find and click "add to cart" button
        Given url of product page to check add to cart
        When add to cart found
        Then we should proceed to checkout

    Scenario: Perform login as guest
        Given Is product page has "login as guest" feature
        When product page support "login as guest" feature
        Then we should perform "login as guest"
    
    @skip_login
    Scenario: Perform login with credentials
        Given Is "login" required
        Then perform "login" with credentials