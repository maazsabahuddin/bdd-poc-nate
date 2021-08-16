Feature: Ecommerce Checkout

    Scenario: Find and click buy now button
        Given url of buy now page
        Then we should land to login page
    
    # @skip_login
    # Scenario: Login with credentials
    #     Given credentials for perfom signin
    #     Then login performed and moved to next step

    # Scenario: Login as guest
    #     Given page with login as guest option
    #     Then we should contine with address details