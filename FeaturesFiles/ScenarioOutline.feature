@Regression

Feature: An example of Scenario Outline with Examples

 Scenario Outline: Sauce Labs Difff login
   Given the user launches the application
   When the user verifies the logo
   When the user enters "<username>" in username field
   Then the user enters "<password>" in password field
   And the user clicks on login button



   Examples:
     | username |password|
      |standard_user|secret_sauce|
     |locked_out_user|secret_sauce|
     |problem_user|secret_sauce|
     |performance_glitch_user|secret_sauce|