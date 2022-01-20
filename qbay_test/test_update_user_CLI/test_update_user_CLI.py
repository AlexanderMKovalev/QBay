import os
from pathlib import Path
import subprocess
from qbay.models import User, Product
from qbay.models import db

# Input Partitioning testing method: Input partitioning

# get expected input/output file
current_folder = Path(__file__).parent
working_dir = Path(__file__).parent.parent.parent

db.session.query(User).delete()
db.session.query(Product).delete()
db.session.commit()
db.session.close()

# Input Partitioning testing, R3-4: Username Tests

# A valid update for username
valid_username_in = open(current_folder.joinpath(
    'valid_username.in'))
valid_username_out = open(current_folder.joinpath(
    'valid_username.out')).read()


def test_update_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=valid_username_in,
        capture_output=True, text=True
    ).stdout

    with open("Output.txt", "w") as file1:
        file1.write(output)

    assert output.strip() == valid_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-4: Username cannot be too short
too_short_username_in = open(current_folder.joinpath(
    'too_short_username.in'))
too_short_username_out = open(current_folder.joinpath(
    'too_short_username.out')).read()


def test_too_short_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_short_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == too_short_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-4: Username cannot be too long
too_long_username_in = open(current_folder.joinpath(
    'too_long_username.in'))
too_long_username_out = open(current_folder.joinpath(
    'too_long_username.out')).read()


def test_too_long_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_long_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == too_long_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-4: Username cannot be non alphanumeric
non_alphanumeric_username_in = open(current_folder.joinpath(
    'non_alphanumeric_username.in'))
non_alphanumeric_username_out = open(current_folder.joinpath(
    'non_alphanumeric_username.out')).read()


def test_non_alphanumeric_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=non_alphanumeric_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == non_alphanumeric_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-4: Username cannot have space suffix
space_suffix_username_in = open(current_folder.joinpath(
    'space_suffix_username.in'))
space_suffix_username_out = open(current_folder.joinpath(
    'space_suffix_username.out')).read()


def test_space_suffix_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=space_suffix_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == space_suffix_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-4: Username cannot have space prefix
space_prefix_username_in = open(current_folder.joinpath(
    'space_prefix_username.in'))
space_prefix_username_out = open(current_folder.joinpath(
    'space_prefix_username.out')).read()


def test_space_prefix_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=space_prefix_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == space_prefix_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing,
# R3-4: Username can have a space that is Not prefix or suffix
valid_space_username_in = open(current_folder.joinpath(
    'valid_space_username.in'))
valid_space_username_out = open(current_folder.joinpath(
    'valid_space_username.out')).read()


def test_valid_space_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=valid_space_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == valid_space_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R2-2: A valid update for Address
valid_address_in = open(current_folder.joinpath(
    'valid_address.in'))
valid_address_out = open(current_folder.joinpath(
    'valid_address.out')).read()


def test_update_address():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=valid_address_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == valid_address_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R2-2: Address should not be empty
empty_address_in = open(current_folder.joinpath(
    'empty_address.in'))
empty_address_out = open(current_folder.joinpath(
    'empty_address.out')).read()


def test_empty_address():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=empty_address_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == empty_address_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R2-2: Address should be alphnumeric
not_alphanumeric_address_in = open(current_folder.joinpath(
    'not_alphanumeric_address.in'))
not_alphanumeric_address_out = open(current_folder.joinpath(
    'not_alphanumeric_address.out')).read()


def test_not_alphanumeric_address():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=not_alphanumeric_address_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == not_alphanumeric_address_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-3: A valid update for Postal Code
valid_postal_code_in = open(current_folder.joinpath(
    'valid_postal_code.in'))
valid_postal_code_out = open(current_folder.joinpath(
    'valid_postal_code.out')).read()


def test_update_postal_code():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=valid_postal_code_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == valid_postal_code_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-3: Postal code invalid format
invalid_format_postal_code_in = open(current_folder.joinpath(
    'invalid_format_postal_code.in'))
invalid_format_postal_code_out = open(current_folder.joinpath(
    'invalid_postal_code.out')).read()


def test_invalid_format_postal_code():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=invalid_format_postal_code_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == invalid_format_postal_code_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-3: Postal code too short
too_short_postal_code_in = open(current_folder.joinpath(
    'too_short_postal_code.in'))
too_short_postal_code_out = open(current_folder.joinpath(
    'invalid_postal_code.out')).read()


def test_too_short_format_postal_code():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_short_postal_code_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == too_short_postal_code_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-3: Postal code too long
too_long_postal_code_in = open(current_folder.joinpath(
    'too_long_postal_code.in'))
too_long_postal_code_out = open(current_folder.joinpath(
    'invalid_postal_code.out')).read()


def test_too_long_postal_code():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_long_postal_code_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == too_long_postal_code_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Input Partitioning testing, R3-3: Postal code using invalid characters
invalid_char_postal_code_in = open(current_folder.joinpath(
    'invalid_char_postal_code.in'))
invalid_char_postal_code_out = open(current_folder.joinpath(
    'invalid_postal_code.out')).read()


def test_invalid_char_postal_code():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=invalid_char_postal_code_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == invalid_char_postal_code_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()
