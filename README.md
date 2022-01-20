# Group-4-web-app
![GitHub All Releases](https://img.shields.io/badge/Build-Passing-green)
![GitHub All Releases](https://img.shields.io/badge/Test%20Coverage-Passing-green)

Repository for CISC 327 web app

	├── LICENSE

	├── README.md
	
	├── requirements.txt
	
	├── qbayDB
	
	├── A0-contract.md

	├── .github

   		└── workflows

			├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)

			└── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)

	├── docs
		
		├── Scrum.md
		
		├── Sprint4 Board.PNG
		
		├── documentation.md
		
		└── pull_request_template.md

	├── qbay                 ======> Application source code

		├── __init__.py      ======> Required for a python module (can be empty)

		├── __main__.py      ======> Program entry point

			└── models.py        ======> Data models
			
			└── cli.py        ======> CLI Pages

	├── qbay_test            ======> Testing code

   		├── __init__.py      ======> Required for a python module (can be empty)
		
			├── test_login
			
				└── test_login.py
				
					├── test_login()
					
					├── test_login_fail()
					
					├── test_login_empty()
					
					├── test_login_email_long()
					
					├── test_login_no_cap()
					
					├── test_login_all_cap()
			
			├── test_register_CLI
			
				└── test_fuzzy_place_order_cli
			
					├── test_fuzzy_place_order_cli.py
				
				└── test_place_order_cli
			
					├── test_place_order_cli.py
									
				└── test_display_order_cli
			
					├── test_display_order_cli.py
			
				└── test_Register_CLI.py
			
					├── test_register()

					├── test_empty_email()

					├── test_used_email()

					├── test_no_at_email()

					├── test_too_many_at_email()

					├── test_too_long_email()

					├── test_underscore_in_domain_email()

					├── test_empty_password()

					├── test_not_match_password()

					├── test_no_uppercase_password()

					├── test_empty_username()

					├── test_too_long_username()

					├── test_non_alphanumeric_username()

					├── test_space_prefix_username()

					├── test_space_suffix_username()
			
			├── test_update_user_CLI
			
				└── test_Register_CLI.pytest_update_user_CLI.py
					
					├── test_update_username()

					├── test_too_short_username()

					├── test_too_long_username()

					├── test_non_alphanumeric_username()

					├── test_update_address()

					├── test_empty_address()

					├── test_not_alphanumeric_address()

					├── test_invalid_format_postal_code()

					├── test_too_short_format_postal_code()

					├── test_invalid_char_postal_code()
					
			├── test_create_product_cli
			
				└──  test_create_product_cli.py
				
					├── test_create_product_alpha_true()
					
					├── test_create_product_alpha_true_with_spaces()
					
					├── test_create_product_not_alpha()
					
					├── test_create_product_spaces_before()
					
					├── test_create_product_spaces_after()
					
					├── test_create_product_no_longer_than_80()
					
					├── test_create_product_longer_than_80()
					
					├── test_create_product_description_min_20()
					
					├── test_create_product_description_max_2000()
					
					├── test_create_product_description_under_20()
					
					├── test_create_product_description_over_2000()
					
					├── test_create_product_description_longer_than_title()
					
					├── test_create_product_description_shorter_than_title()
					
					├── test_create_product_price_min_10()
					
					├── test_create_product_price_max_10000()
					
					├── test_create_product_price_under_10()
					
					├── test_create_product_price_over_10000()
					
					├── test_create_product_last_modified_date_valid()
					
					├── test_create_product_owner_email_exists()
					
					├── test_create_product_not_same_title()
					
					├── test_create_product_same_title()
					
					
			
			├── test_update_product_CLI
			
				└──  update_product_CLI.py
					
					├── test_update_product_date()
					
					├── test_update_product_date_wrong()
					
					├── test_update_product_title()
					
					├── test_update_product_title_incorrect()
					
					├── test_update_product_description()
					
					├── test_update_product_description_incorrect()
					
					├── test_update_product_price()
					
					├── test_update_product_price_too_low()
					
					├── test_update_product_price_decreases()

   		├── test_Login.py	===> backend tests for login
		
		├── test_Product.py	===> backend tests for product
		
		├── test_Register.py	===> backend tests for registering a user
		
		├── test_Update.py	===> backend tests forupdating user
		
		├── test_Login.py	===> backend tests for login

   		└── test_update_product.py   ======> backend tests for updating product

	└── requirements.txt     ======> Dependencies
