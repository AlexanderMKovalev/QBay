import os
from pathlib import Path
import subprocess
from qbay.models import User
from qbay.models import Product
from qbay.models import db
from string import Template

# Blackbox testing method - Robustness/Boundary Testing

# get expected input/output file
current_folder = Path(__file__).parent
working_dir = Path(__file__).parent.parent.parent


# read expected in/out
expected_in = open(current_folder.joinpath(
    'title_alphanumeric.in'))

expected_out = open(current_folder.joinpath(
    'title_alphanumeric.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-1: The title of the product has to be
# alphanumeric-only


def test_create_product_alpha_true():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

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


# read expected in/out
expected_in2 = open(current_folder.joinpath(
    'title_alphanumeric_with_space.in'))

expected_out2 = open(current_folder.joinpath(
    'title_alphanumeric_with_space.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-1: The title of the product has to be
# alphanumeric-only with spaces not as first or last characters


def test_create_product_alpha_true_with_spaces():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in2,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out2 = Template(expected_out2)
    modified_expected_out2 = modified_expected_out2.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out2.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in3 = open(current_folder.joinpath(
    'title_not_alphanumeric.in'))

expected_out3 = open(current_folder.joinpath(
    'title_not_alphanumeric.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-1: The title of the product is not
# alphanumeric


def test_create_product_not_alpha():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in3,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out3.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in4 = open(current_folder.joinpath(
    'title_spaces_before.in'))

expected_out4 = open(current_folder.joinpath(
    'title_spaces_before.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-1: The title of the product has spaces before
# the characters


def test_create_product_spaces_before():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in4,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out4.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in5 = open(current_folder.joinpath(
    'title_spaces_after.in'))

expected_out5 = open(current_folder.joinpath(
    'title_spaces_after.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-1: The title of the product has spaces after
# the characters


def test_create_product_spaces_after():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in5,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out5.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in6 = open(current_folder.joinpath(
    'title_no_longer_than_80.in'))

expected_out6 = open(current_folder.joinpath(
    'title_no_longer_than_80.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-2: The title of the product is no longer than
# 80 characters


def test_create_product_no_longer_than_80():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in6,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out6 = Template(expected_out6)
    modified_expected_out6 = modified_expected_out6.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out6.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in7 = open(current_folder.joinpath(
    'title_longer_than_80.in'))

expected_out7 = open(current_folder.joinpath(
    'title_longer_than_80.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-2: The title of the product is longer than
# 80 characters


def test_create_product_longer_than_80():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in7,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out7.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in8 = open(current_folder.joinpath(
    'description_min_20.in'))

expected_out8 = open(current_folder.joinpath(
    'description_min_20.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-3: The description of the product can be
# arbitrary characters with a minimum length of 20 characters and a maximum
# of 2000 characters (min 20 test)


def test_create_product_description_min_20():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in8,
        capture_output=True, text=True
    ).stdout
    product = Product.query.first()
    modified_expected_out8 = Template(expected_out8)
    modified_expected_out8 = modified_expected_out8.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out8.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in9 = open(current_folder.joinpath(
    'description_max_2000.in'))

expected_out9 = open(current_folder.joinpath(
    'description_max_2000.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-3: The description of the product can be
# arbitrary characters with a minimum length of 20 characters and a maximum
# of 2000 characters (max 2000 test)


def test_create_product_description_max_2000():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in9,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out9 = Template(expected_out9)
    modified_expected_out9 = modified_expected_out9.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out9.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in10 = open(current_folder.joinpath(
    'description_under_20.in'))

expected_out10 = open(current_folder.joinpath(
    'description_under_20.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-3: The description of the product less than
# 20 characters


def test_create_product_description_under_20():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in10,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out10.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in11 = open(current_folder.joinpath(
    'description_over_2000.in'))

expected_out11 = open(current_folder.joinpath(
    'description_over_2000.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-3: The description of the product
# over 2000 characters


def test_create_product_description_over_2000():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in11,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out11.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in12 = open(current_folder.joinpath(
    'description_longer_than_title.in'))

expected_out12 = open(current_folder.joinpath(
    'description_longer_than_title.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-4: The description of the product
# must be longer than the title


def test_create_product_description_longer_than_title():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in12,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out12 = Template(expected_out12)
    modified_expected_out12 = modified_expected_out12.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out12.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in13 = open(current_folder.joinpath(
    'description_shorter_than_title.in'))

expected_out13 = open(current_folder.joinpath(
    'description_shorter_than_title.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-4: The description of the product
# is shorter than the title


def test_create_product_description_shorter_than_title():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in13,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out13.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in14 = open(current_folder.joinpath(
    'price_min_10.in'))

expected_out14 = open(current_folder.joinpath(
    'price_min_10.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-5: The price of the product must be between
# 10 and 10000 inclusive (min 10 test)


def test_create_product_price_min_10():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in14,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out14 = Template(expected_out14)
    modified_expected_out14 = modified_expected_out14.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out14.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in15 = open(current_folder.joinpath(
    'price_max_10000.in'))

expected_out15 = open(current_folder.joinpath(
    'price_max_10000.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-5: The price of the product must be between
# 10 and 10000 inclusive (max 10000 test)


def test_create_product_price_max_10000():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in15,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out15 = Template(expected_out15)
    modified_expected_out15 = modified_expected_out15.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out15.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in16 = open(current_folder.joinpath(
    'price_under_10.in'))

expected_out16 = open(current_folder.joinpath(
    'price_under_10.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-5: The price of the product is under 10
# (under 10 test)


def test_create_product_price_under_10():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in16,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out16.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in17 = open(current_folder.joinpath(
    'price_over_10000.in'))

expected_out17 = open(current_folder.joinpath(
    'price_over_10000.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-5: The price of the product is over 10000
# (over 10000 test)


def test_create_product_price_over_10000():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in17,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out17.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in18 = open(current_folder.joinpath(
    'last_modified_date_valid.in'))

expected_out18 = open(current_folder.joinpath(
    'last_modified_date_valid.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-6: The last modified date of the product is
# between 2021-01-02 and 2025-01-02


def test_create_product_last_modified_date_valid():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in18,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out18 = Template(expected_out18)
    modified_expected_out18 = modified_expected_out18.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out18.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in19 = open(current_folder.joinpath(
    'owner_email_exists.in'))

expected_out19 = open(current_folder.joinpath(
    'owner_email_exists.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-7: Owner_email exists for product


def test_create_product_owner_email_exists():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in19,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out19 = Template(expected_out19)
    modified_expected_out19 = modified_expected_out19.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out19.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in20 = open(current_folder.joinpath(
    'not_same_title.in'))

expected_out20 = open(current_folder.joinpath(
    'not_same_title.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-8: A User cannot create products that have
# the same title


def test_create_product_not_same_title():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in20,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out20 = Template(expected_out20)
    modified_expected_out20 = modified_expected_out20.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out20.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
expected_in21 = open(current_folder.joinpath(
    'same_title.in'))

expected_out21 = open(current_folder.joinpath(
    'same_title.out')).read()


# clear users and products from database
db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Robustness/Boundary Testing, R4-8: A User create products that have
# the same title


def test_create_product_same_title():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in21,
        capture_output=True, text=True
    ).stdout

    product = Product.query.first()
    modified_expected_out21 = Template(expected_out21)
    modified_expected_out21 = modified_expected_out21.safe_substitute(
        last_modified_date=product.last_modified_date)

    assert output.strip() == modified_expected_out21.strip()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
