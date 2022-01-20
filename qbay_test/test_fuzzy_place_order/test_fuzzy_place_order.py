from pathlib import Path
from qbay.models import User, Product, place_an_order
from qbay.models import db
from datetime import datetime

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

payload = open(current_folder.joinpath(
    'payload.txt'))


# Fuzzy Test for Product Title for ordering function
def test_fuzzy_order_title():
    user = User("owner@email.com", "MyTestUsername", "Password!",
                "owner", "lastname")
    user2 = User("sample@email.com", "username1", "Password!",
                 "firstname", "lastname")
    db.session.add(user)
    db.session.add(user2)
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    for line in payload:
        try:
            place_an_order(line, "sample@email.com", 100)
            print(line)
        except Exception:
            continue

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Fuzzy Test for email for ordering function
def test_fuzzy_order_email():
    user = User("owner@email.com", "MyTestUsername", "Password!",
                "owner", "lastname")
    db.session.add(user)
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    for line in payload:
        try:
            place_an_order('Mittens', line, 100)
            print(line)
        except Exception:
            continue

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Fuzzy Test for bal for ordering function
def test_fuzzy_order_bal():
    user = User("owner@email.com", "MyTestUsername", "Password!",
                "owner", "lastname")
    db.session.add(user)
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    for line in payload:
        try:
            place_an_order('Mittens', "sample@email.com", line)
            print(line)
        except Exception:
            continue

    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
