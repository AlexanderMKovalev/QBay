import os
from pathlib import Path
import subprocess
from qbay.models import User, Product
from qbay.models import db
from string import Template


# Input partitioning
# get expected input/output file


current_folder = Path(__file__).parent
working_dir = Path(__file__).parent.parent.parent

db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# R4: A sold product will not be shown on the other user's user interface.
# Output Partioning
# A test that creates three users, creates a product for user1
# Sells it to user2 on the market place and sees if a random user (user3)
# can see if that product is sold
# They Should Not


user_cant_see_in = open(current_folder.joinpath(
    'user_cant_see.in'))
user_cant_see_out = open(current_folder.joinpath(
    'user_cant_see.out')).read()


def test_user_cant_see_sold_product():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=user_cant_see_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(user_cant_see_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# R4: A sold product will not be shown on the other user's user interface.
# Output Partioning
# A test that creates three users, creates a product for user1
# Sells it to user2 on the market place and sees if the buyer can see
# if that product is sold
# They Should Not
buyer_cant_see_in = open(current_folder.joinpath(
    'buyer_cant_see.in'))
buyer_cant_see_out = open(current_folder.joinpath(
    'buyer_cant_see.out')).read()


def test_buyer_cant_see_sold_product():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=buyer_cant_see_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(buyer_cant_see_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# R5: A sold product can be shown on the owner's user interface.
# Output Partioning
# A test that creates three users, creates a product for user1
# Sells it to user2 on the market place and sees if the seller can see
# if their sold product is sold
# They Should
seller_can_see_in = open(current_folder.joinpath(
    'seller_can_see.in'))
seller_can_see_out = open(current_folder.joinpath(
    'seller_can_see.out')).read()


def test_seller_can_see_sold_product():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=seller_can_see_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(seller_can_see_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
