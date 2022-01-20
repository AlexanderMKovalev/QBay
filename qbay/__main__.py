from .cli import login_page, register_page, user_home_page

# create main navigation page


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. Or type 2 to register. \n'
            'Or type q to quit: ')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                user_home_page(user)
            else:
                print('login failed')
        elif selection == '2':
            register_page()
        elif selection == 'q':
            break


if __name__ == '__main__':
    main()
