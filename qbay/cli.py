from .models import login_user, create_user, update_user, Product, \
    create_product, update_product, place_an_order

# let the user input email and password to login


def login_page():
    while True:
        email = input('Please input email to login:')
        password = input('Please input password:')
        try:
            return login_user(email, password)
        except Exception as e:
            print(str(e))
            print('Login failed please try again\n')
            quit = input(
                'Type y to continue login/ type n to go to welcome page:')
            if quit == 'y':
                continue
            elif quit == 'n':
                break


# register user by input email and password two times


def register_page():
    # Loop to ask user to try again until valid
    while True:
        try:
            email = input('Please input email:')
            # Username is set to portion of email as default
            username = input('Please input a username:')
            password = input('Please input password:')
            password_twice = input('Please input the password again:')
            first_name = input('Please input your first name:')
            last_name = input('Please input your last name:')
            if password != password_twice:
                raise ValueError('Password entered not the same')
            create_user(email, username, password, first_name, last_name)
            print('Registration succeeded')
            break
        except Exception as e:
            print(str(e))
            print('Registration failed.')
            quit = input("Try again? (y/n) ")
            if quit == 'n':
                break
            else:
                continue


# update user profile by selecting a number related to profile information


def update_user_page(user):
    while True:
        selection = input(
            '\nPlease type 1 to update username,'
            '\nType 2 to update shipping address,'
            '\nType 3 to update postal code, '
            '\nType q to go back: ')
        if selection == '1':
            while True:
                try:
                    username = input('Please input new username: ')
                    update_user(user.email, selection, username)
                    print('Update username successful')
                except Exception as e:
                    print('Update username failed')
                    print(str(e))
                    quit = input("Try again? (y/n) ")
                    if quit == 'n':
                        break
                    else:
                        continue
                break

        elif selection == '2':
            while True:
                try:
                    shipping_address = input('Please input '
                                             'new shipping address: ')
                    update_user(user.email, selection, shipping_address)
                    print('Update shipping address successful')
                except Exception as e:
                    print('Update shipping address failed')
                    print(str(e))
                    quit = input("Try again? (y/n) ")
                    if quit == 'n':
                        break
                    else:
                        continue
                break

        elif selection == '3':
            while True:
                try:
                    postal_code = input('Please input new postal code: ')
                    update_user(user.email, selection, postal_code)
                    print('Update postal code successful')
                except Exception as e:
                    print('Update postal code failed')
                    print(str(e))
                    quit = input("Try again? (y/n) ")
                    if quit == 'n':
                        break
                    else:
                        continue
                break

        elif selection == 'q':
            break

# User home page with links to product creation page and product update page


def user_home_page(user):
    while True:
        print("\nWelcome", user.userFirstName, user.userLastName, "\n")
        print("Your current balance is", user.balance, "\n")
        print("All your current products:\n")
        user_products = Product.query.filter_by(owner_email=user.email).all()
        if len(user_products) > 0:
            for product in user_products:
                print("Title:", product.title)
                print("Description:", product.description)
                print("Price:", product.price)
                print("Last modified Date:", product.last_modified_date)
                print("Sold:", product.sold)
                print("\n")
        else:
            print("No products to display.\n")

        selection = input("Type 1 to create a new product\n"
                          "Type 2 to update an existing product\n"
                          "Type 3 to update user profile\n"
                          "Type 4 to see profile details\n"
                          "Type 5 to view the marketplace\n"
                          "Type q to sign out:")
        selection = selection.strip()

        if selection == '1':
            product_creation_page(user)
        elif selection == '2':
            product_update_page(user)
        elif selection == '3':
            update_user_page(user)
        elif selection == '4':
            print("\nProfile Details")
            print("-" * 50)
            print("Username:", user.user_name, "\n"
                  "First name:", user.userFirstName, "\n"
                  "Last name:", user.userLastName, "\n"
                  "Email:", user.email, "\n"
                  "Balance:", user.balance, "\n"
                  "Shipping Address:", user.shipping_address, "\n"
                  "Postal Code:", user.postal_code, "\n")
            print("-" * 50)
        elif selection == '5':
            marketplace_page(user)
        elif selection == 'q':
            print("Thank you for visiting, signing out...\n")
            break


# Product creation page


def product_creation_page(user):
    print("Product Creation Page")
    print("-" * 50)
    stay_on_page = True
    while stay_on_page:
        title = input("Enter a product title:")
        description = input("Enter a product description:")
        valid_price = False
        while not valid_price:
            try:
                price = float(input("Enter a product price:"))
                valid_price = True
            except ValueError:
                print("Not a valid price try again.")

        if create_product(title, description, price, user.email):
            print("Product sucessfully created!")
            valid_selection = False
            while (not valid_selection):
                selection = input("Would you like to create another product?\n"
                                  "Type y for yes and q to quit the product"
                                  " creation page:")
                if selection == 'y':
                    valid_selection = True
                elif selection == 'q':
                    valid_selection = True
                    stay_on_page = False
        else:
            while True:
                choice = input("Product could not be created. Press q to quit"
                               " or y to try again:")
                if choice == 'q':
                    stay_on_page = False
                    break
                if choice == 'y':
                    stay_on_page = True
                    break
                else:
                    continue

# Product update page


def product_update_page(user):
    while True:
        user_products = Product.query.filter_by(owner_email=user.email).all()
        if len(user_products) == 0:
            print(
                "\n No products, add a product and try again :p")
            return None
        else:
            print("\nWelcome, to product update!\n")
            print("Which product do you wish to update?\n")

            i = 1
            for p in user_products:
                print(str(i) + ". " + p.title + "\n")
                i = i + 1
            choice = input(
                "Please press some number to select a product or q to quit.\n")

            if choice == 'q':
                return None

            productIndex = int(choice)
            if ((1 > productIndex) or (productIndex > len(user_products))):
                print("Selection is not valid true again :p")
                continue

            product = user_products[productIndex - 1]
            break

    while True:
        selection = input(
            '\nPlease type 1 to update title,'
            '\nType 2 to update description,'
            '\nType 3 to update price, '
            '\nType q to go back: ')
        if selection == '1':
            while True:
                title = input('Please input new title: ')
                succsess = update_product(product.title, title,
                                          product.description, product.price)
                if succsess:
                    print('Update title successful')
                    break
                else:
                    print('Update title failed')
                    continue

        elif selection == '2':
            while True:
                description = input('Please input '
                                    'new description: ')
                succsess = update_product(product.title, product.title,
                                          description, product.price)
                if succsess:
                    print('Update description successful')
                    break
                else:
                    print('Update description failed')
                    continue

        elif selection == '3':
            while True:

                # Continuosly ask for the price
                while True:
                    try:
                        price = float(input("Enter a product price:"))
                        break
                    except ValueError:
                        print("Not a valid price try again.")

                succsess = update_product(product.title, product.title,
                                          product.description, price)
                if succsess:
                    print('Update price successful')
                    break
                else:
                    print('Update price failed')
                    continue

        elif selection == 'q':
            break


# Marketplace page


def marketplace_page(user):
    while True:
        print("\nMARKETPLACE")
        print("-" * 50)
        all_products = Product.query.filter_by(sold=False).all()
        if len(all_products) == 0:
            print("\n No products in the marketplace.")
            return None
        else:
            print("Balance:", user.balance, "\n")
            for product in all_products:
                print("\nTitle:", product.title)
                print("Description:", product.description)
                print("Price:", product.price)
                print("Last modified Date:", product.last_modified_date)
                print("Owner-email:", product.owner_email)
                print("\n")
        selection = input("Type the title of the product to buy it.\n"
                          "Press q to quit:")
        place_an_order(selection, user.email, user.balance)
        if selection == 'q':
            break
