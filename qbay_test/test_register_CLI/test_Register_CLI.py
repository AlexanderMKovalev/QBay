import os
from pathlib import Path
import subprocess
from qbay.models import User
from qbay.models import db

# Black Box testing method: Input partitioning

# get expected input/output file
current_folder = Path(__file__).parent
working_dir = Path(__file__).parent.parent.parent

db.session.query(User).delete()
db.session.commit()
db.session.close()

# A valid registration
expected_in = open(current_folder.joinpath(
    'valid.in'))
expected_out = open(current_folder.joinpath(
    'valid.out')).read()


def test_register():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == expected_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Email Tests

# Email cannot be empty
empty_email_in = open(current_folder.joinpath(
    'empty_email.in'))
empty_email_out = open(current_folder.joinpath(
    'empty_email.out')).read()


def test_empty_email():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=empty_email_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == empty_email_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Email cannot have already been used (Must be unique)
used_email_in = open(current_folder.joinpath(
    'used_email.in'))
used_email_out = open(current_folder.joinpath(
    'used_email.out')).read()


def test_used_email():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=used_email_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == used_email_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Emails with no @ are not accepted.
no_at_email_in = open(current_folder.joinpath(
    'no_at_email.in'))
no_at_email_out = open(current_folder.joinpath(
    'no_at_email.out')).read()


def test_no_at_email():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=no_at_email_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == no_at_email_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Emails too many @ are not accepted.
too_many_at_email_in = open(current_folder.joinpath(
    'too_many_at_email.in'))
too_many_at_email_out = open(current_folder.joinpath(
    'too_many_at_email.out')).read()


def test_too_many_at_email():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_many_at_email_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == too_many_at_email_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Emails that are too long not accepted.
too_long_email_in = open(current_folder.joinpath(
    'too_long_email.in'))
too_long_email_out = open(current_folder.joinpath(
    'too_long_email.out')).read()


def test_too_long_email():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=too_long_email_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == too_long_email_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Email with underscore in domain not accepted
underscore_in_domain_email_in = open(current_folder.joinpath(
    'underscore_in_domain_email.in'))
underscore_in_domain_email_out = open(current_folder.joinpath(
    'underscore_in_domain_email.out')).read()


def test_underscore_in_domain_email():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=underscore_in_domain_email_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == underscore_in_domain_email_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Password Tests

# Passwords cannot be too short
empty_password_in = open(current_folder.joinpath(
    'empty_password.in'))
empty_password_out = open(current_folder.joinpath(
    'empty_password.out')).read()


def test_empty_password():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=empty_password_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == empty_password_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Passwords must match
not_match_password_in = open(current_folder.joinpath(
    'not_match_password.in'))
not_match_password_out = open(current_folder.joinpath(
    'not_match_password.out')).read()


def test_not_match_password():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=not_match_password_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == not_match_password_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Passwords must have an uppercases
no_uppercase_password_in = open(current_folder.joinpath(
    'no_uppercase_password.in'))
no_uppercase_password_out = open(current_folder.joinpath(
    'no_uppercase_password.out')).read()


def test_no_uppercase_password():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=no_uppercase_password_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == no_uppercase_password_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Passwords must have a lower case
no_lowercase_password_in = open(current_folder.joinpath(
    'no_lowercase_password.in'))
no_lowercase_password_out = open(current_folder.joinpath(
    'no_lowercase_password.out')).read()


def test_no_lowercase_password():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=no_lowercase_password_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == no_lowercase_password_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Passwords must have a special character
no_specialchar_password_in = open(current_folder.joinpath(
    'no_specialchar_password.in'))
no_specialchar_password_out = open(current_folder.joinpath(
    'no_specialchar_password.out')).read()


def test_no_specialchar_password():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=no_specialchar_password_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == no_specialchar_password_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Username Tests
# Username cannot be too short
empty_username_in = open(current_folder.joinpath(
    'empty_username.in'))
empty_username_out = open(current_folder.joinpath(
    'empty_username.out')).read()


def test_empty_username():
    # pip the input
    os.chdir(working_dir)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=empty_username_in,
        capture_output=True, text=True
    ).stdout

    assert output.strip() == empty_username_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# Username cannot be too long
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


# Username cannot be non alphanumeric
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


# Username cannot have space suffix
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


# Username cannot have space prefix
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
