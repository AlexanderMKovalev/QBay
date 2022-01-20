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


# R1: A user can place an order on the products
# A valid order
expected_in = open(current_folder.joinpath(
    'valid.in'))
expected_out = open(current_folder.joinpath(
    'valid.out')).read()


def test_valid_order():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(expected_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# Title
# empty title
empty_title_in = open(current_folder.joinpath(
    'empty_title.in'))
empty_title_out = open(current_folder.joinpath(
    'empty_title.out')).read()


def test_title_empty_order():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=empty_title_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(empty_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# not alphanumeric title
not_alphanumeric_title_in = open(current_folder.joinpath(
    'not_alphanumeric_title.in'))
not_alphanumeric_title_out = open(current_folder.joinpath(
    'not_alphanumeric_title.out')).read()


def test_title_not_alphanumeric_order():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=not_alphanumeric_title_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(not_alphanumeric_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# too long title
too_long_title_in = open(current_folder.joinpath(
    'too_long_title.in'))
too_long_title_out = open(current_folder.joinpath(
    'too_long_title.out')).read()


def test_title_too_long_order():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_long_title_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(too_long_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# space prefix title
space_prefix_title_in = open(current_folder.joinpath(
    'space_prefix_title.in'))
space_prefix_title_out = open(current_folder.joinpath(
    'space_prefix_title.out')).read()


def test_title_space_prefix_order():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=space_prefix_title_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(space_prefix_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# space suffix title
space_suffix_title_in = open(current_folder.joinpath(
    'space_suffix_title.in'))
space_suffix_title_out = open(current_folder.joinpath(
    'space_suffix_title.out')).read()


def test_title_space_suffix_order():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=space_suffix_title_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(space_suffix_title_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# R2: A user cannot place an order for his/her products
buy_own_in = open(current_folder.joinpath(
    'buy_own.in'))
buy_own_out = open(current_folder.joinpath(
    'buy_own.out')).read()


def test_email_equals_owner():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=buy_own_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(buy_own_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# R3: A user cannot place an order that costs more than his/her balance
bal_less_price_in = open(current_folder.joinpath(
    'bal_less_price.in'))
bal_less_price_out = open(current_folder.joinpath(
    'bal_less_price.out')).read()


def test_bal_less_price():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=bal_less_price_in,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out = Template(bal_less_price_out)
    modified_expected_out = modified_expected_out.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
