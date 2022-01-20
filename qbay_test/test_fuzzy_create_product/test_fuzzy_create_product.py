from pathlib import Path
from qbay.models import User, create_user
from qbay.models import Product, create_product
from qbay.models import db

# Testing method: Fuzzy Testing
# Tests for creating the product

# get expected input/output file
current_folder = Path(__file__).parent
working_dir = Path(__file__).parent.parent.parent

# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Fuzzy Test for Product Title for product creation function
payload = open(current_folder.joinpath(
    'payload.txt'))


def test_fuzzy_product_create_title():
    create_user("testUser1@gmail.com", "testUser", "Pswd123!", "user", "test")
    for line in payload:
        try:
            create_product(line, "Some Mittens what can I say",
                           50, "testUser1@gmail.com", True)

            # Print the payload that is successful, ignore others
            print(line)
        except Exception:
            continue

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()

# Fuzzy Test for Product Description for product creation function


def test_fuzzy_product_create_description():
    create_user("testUser2@gmail.com", "testUser", "Pswd123!", "user", "test")
    i = 0
    for line in payload:
        try:
            create_product("Mittens" + str(i), line,
                           50, "testUser2@gmail.com", True)
            # Print the payload that is successful, ignore others
            print(line)
        except Exception:
            continue
        i = i + 1

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()

# Fuzzy Test for Product Price for product creation function


def test_fuzzy_product_create_price():
    create_user("testUser3@gmail.com", "testUser", "Pswd123!", "user", "test")
    for line in payload:
        try:
            create_product("Mittens", "Some Mittens what can I say",
                           line, "testUser3@gmail.com", True)

            # Print the payload that is successful, ignore others
            print(line)
        except Exception:
            continue

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()

# Fuzzy Test for Product Email for product creation function


def test_fuzzy_product_create_email():
    # Create user to associate products with
    create_user("testUser4@gmail.com", "testUser", "Pswd123!", "user", "test")
    for line in payload:
        try:
            create_product("Mittens", "Some Mittens what can I say",
                           50, line, True)

            # Print the payload that is successful, ignore others
            print(line)
        except Exception:
            continue

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
