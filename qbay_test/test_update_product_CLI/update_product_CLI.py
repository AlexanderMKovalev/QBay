import os
from pathlib import Path
import subprocess
from qbay.models import User
from qbay.models import Product
from qbay.models import db
from string import Template

# Black Box testing method: Output partitioning
# Tests for updating the product

# get expected input/output file
current_folder = Path(__file__).parent
working_dir = Path(__file__).parent.parent.parent

# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Output partitioning R5-3: Modify date correctly
correct_date_in = open(current_folder.joinpath(
    'correct_date.in'))
correct_date_out = open(current_folder.joinpath(
    'correct_date.out')).read()


def test_update_product_date():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=correct_date_in,
        capture_output=True, text=True
    ).stdout
    product = Product.query.first()
    modified_expected_out = Template(correct_date_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
    print("done")


# Output partitioning R5-3: Modify date incorrectly
incorrect_date_in = open(current_folder.joinpath(
    'incorrect_date.in'))
incorrect_date_out = open(current_folder.joinpath(
    'incorrect_date.out')).read()


def test_update_product_date_wrong():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=incorrect_date_in,
        capture_output=True, text=True
    ).stdout
    product = Product.query.first()
    modified_expected_out = Template(incorrect_date_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    text_file = open("Output.txt", "w")
    text_file.write(output)
    text_file.close()

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
    print("done")


# Output partitioning R5-1, R5-4: Update title correctly
correct_title_input = open(current_folder.joinpath(
    'correct_title.in'))
correct_title_out = open(current_folder.joinpath(
    'correct_title.out')).read()


def test_update_product_title():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=correct_title_input,
        capture_output=True, text=True
    ).stdout
    product = Product.query.first()
    modified_expected_out = Template(correct_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Output partitioning R5-1, R5-4: Update title fail
incorrect_title_input = open(current_folder.joinpath(
    'incorrect_title.in'))
incorrect_title_out = open(current_folder.joinpath(
    'incorrect_title.out')).read()


def test_update_product_title_incorrect():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=incorrect_title_input,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(incorrect_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Output partitioning R5-1, R5-4: Update description correctly
correct_description_input = open(current_folder.joinpath(
    'correct_description.in'))
correct_description_out = open(current_folder.joinpath(
    'correct_description.out')).read()


def test_update_product_description():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=correct_description_input,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(correct_description_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Output partitioning R5-1, R5-4: Update description fail
incorrect_description_input = open(current_folder.joinpath(
    'incorrect_description.in'))
incorrect_description_out = open(current_folder.joinpath(
    'incorrect_description.out')).read()


def test_update_product_description_incorrect():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=incorrect_description_input,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(incorrect_description_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Black Box testing method: Input partitioning


# Input partitioning R5-2, Update price correctly
correct_price_input = open(current_folder.joinpath(
    'correct_price.in'))
correct_price_out = open(current_folder.joinpath(
    'correct_price.out')).read()


def test_update_product_price():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=correct_price_input,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(correct_price_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Input partitioning R5-2: Update price, price too low
price_too_low_input = open(current_folder.joinpath(
    'price_too_low.in'))
price_too_low_out = open(current_folder.joinpath(
    'price_too_low.out')).read()


def test_update_product_price_too_low():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=price_too_low_input,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(price_too_low_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Input partitioning R5-2: Update price, price decreases
price_decreases_input = open(current_folder.joinpath(
    'price_decreases.in'))
price_decreases_out = open(current_folder.joinpath(
    'price_decreases.out')).read()


def test_update_product_price_decreases():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=price_decreases_input,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(price_decreases_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
