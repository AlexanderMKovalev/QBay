# Scrum Meeting 
## Date Meeting Held: Wednesday November 3rd 2021

## Everyone's branches:
Marc: create_cli_tests_create_product, update_product_error_message

Aim: test_login_frontend

Claire: register_CLI_test

Alex: update_product_cli

## Progress:
Aim worked on the login tests and has made tests for when the login fails and succeeds. She isn't sure if she needs to add more tests.  
Claire wrote tree tests, (1) valid inputs, (2) empty email, (3) empty password all three have expected outputs.
Alex wrote two pains of negative and positive tests for R5-1, for the title and description of the product.
Marc wrote a negative and positive test for R4-1.

## Difficulties:
Claire encountered permanent loop in that occurred with testing invalid registration. She had already fixed it!
Marc and Alex are encountering difficulties getting correct spacing between the expected and actual output.

## Plan:
Aim plans to write tests to handle different types of login failure and finish up all test cases and document the change before the deadline.
Claire plans on finishing the input partition for email input tonight. Either later or tomorrow moving on to password, then username.
Tomorrow morning she plans to create the files for update and list of tests that are needed. Later in day and Friday she plans to write the tests.
Marc plans on finishing all of his tests following the blackbox testing method.
Alex is planning on finishing all of his tests by friday.

## Date Meeting Held: Wednesday November 17th 2021
## Everyone's branches:

Alex: fuzzy_test_product

Marc: ship_system

Aim: Container

Claire: fuzzyTestRegister

## Progress:

Claire has created branch and three tests. Tests are not fully complete.

Aim has finished docker set up, build and run the image. I also pushed the image on to dockerhub for others to access. 

Marc has changed the default image in the docker compose file to point to our own image.
any difficulties.

Alex has written all of his tests but is unsure if they are correct, is awaiting response from the proffesor.

## Plan:

Marc's plan is to make sure that system once entire system is deployed including the integration of fuzzy testing that it works properly.

Alex is planning on slighly adjusting his tests before merging.

Claire's plan is to finish the tests in progress + 2 more nov 18 so team can review. Review code for team.

Aim's plan is to make sure the deployment is done.

## Date Meeting Held: Monday December 6th 2021
## Everyone's branches:

Aim and Marc: placing_an_order

## Progress:

Aim and Marc got started on adding the ability to place an order on a product.

## Difficulties:

None so far.

## Plan:

Have Aim and Marc complete their tickets and add the ability to place and order and display purchased products.

## Date Meeting Held: Wednesday December 8th 2021

Aim and Marc: placing_an_order

Claire: testfirstthree

## Progress:

Aim and Marc: Finished up making the functionality to add the ability to place an order on a product adn display sold product for the proper users.

Claire Started and finished making the tests for placing orders.

## Difficulties:

We can't merge Aim's and Marc's branches because they have no tests yet but those are assigned to other people.

## Plan:

Have Alex finish his ticket to test displaying products and merge Claire's and Alex's branches to Aim and Marc's branch so that their branch has tests and can be merged by Friday.
