Feature: Ecommerce Checkout


    Scenario: Perform login as guest
        Given Is product page has "login as guest" feature
        When product page support "login as guest" feature
        Then we should perform "login as guest"

    @skip_personal_info
    Scenario: Fill personal information
        Given information required page
        When personal information is required
        Then fill the information and proceed to next step