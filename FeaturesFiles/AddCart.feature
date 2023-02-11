Feature: Add to Cart

  @Regression @Sanity
  Scenario:  Login
    Given the user launches the application
    When the user verifies the logo
    Then the user enters valid credentials
  @Regression
  Scenario: Filter by High to Low
    Given the user verifies the homepage logo
    Then the user filters high to low
  @Sanity
  Scenario: Filter by Low to High
    Given the user verifies the homepage logo
    Then the user filters low to high

  Scenario: Find highest product and place the order
    Given the user verifies the homepage logo
    Then the user clicks on Add to cart button
