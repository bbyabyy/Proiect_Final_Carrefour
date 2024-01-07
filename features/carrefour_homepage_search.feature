Feature: Test the search functionality in the homepage of carrefour

  Background:
    Given Home page: The user is on https://www.carrefour.ro/


  @regression
  Scenario Outline: Check that the user can make a simple in carrefour homepage
    When Home page: The user search for "<product_name>" from search box
    Then  Home Page: The user have at least "<results_number>" results returned
    Examples:
    |product_name  |results_number  |
    |Laptop        |80              |
    |Sampon        |350             |
    |Patiserie     |30              |
    |Vin rosu      |500             |
    |Balsam rufe   |60              |

  @regression
  Scenario: Check that the user can add a product in My basket
    When Home Page: The user type in search box "cafea boabe"
    When Home page: The user clicks the search button
    When Home page: The user navigate to first returned product page
    When Home page: The user clicks on add to basket button
    Then Home page: The user should receive a confirmation that the product has been added to basket

  @regression
  Scenario: Check that the user can remove products from the cart
    When  My basket page: The user clicks on My basket
    When  My basket page: The user clicks on remove product from the cart button
    Then  My basket page: The user receved a message that the basket is emty


  @regression
  Scenario Outline: Check that a user can make an job search form Careers
    When Home page: I click on careers link
    When Careers page: I click  on "<alege oras>" from "Alege oras" box
    When Careers page: I click on "<alege magazin>" from "Alege magazin" box
    When Careers page: I click on Looking for a job button
    Then Careers page: I have at least "<no_of_results>" results returned
    Examples:
    |alege oras  |alege magazin              |no_of_results|
    |Bucuresti   |Carrefour Baneasa          |2            |
    |Brasov      |Market Brasov Onix Grivitei|1
    |Galati      |Express Galati Mazepa      |0            |


  @regression
  Scenario: Check if user can access login page
    When  Home page: The user clicks on account button
    Then  Home page: The user should be redirected to login page

  Scenario: Check if user can login with valid account
    Given Login page: The user is on login page
    When  Login page: The user enters "contul.meu20@yahoo.com" on the username field
    When  Login page: The user enters "_A#YcveC*Mrds5Q" on the password field
    When  Login page: The user clicks on login button
    Then  Login page: User should be logged in