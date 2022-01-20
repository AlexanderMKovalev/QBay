import os
from pathlib import Path
import subprocess
from qbay.models import User
from qbay.models import db

# Black Box testing method: Input partitioning


# get expected input/output file
current_folder = Path(__file__).parent
# define qbay path
qbay1 = Path(__file__).parent.parent.parent

db.session.query(User).delete()
db.session.commit()
db.session.close()

# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_login.in'))
expected_out = open(current_folder.joinpath(
    'test_login.out')).read()

# Black Box testing method: Input partitioning
# R2-1: A user can log in using her/his email address and the password.
# login sucessful and compare output to expected output


def test_login():
    # capsys -- object created by pytest to
    # capture stdout and stderr
    os.chdir(qbay1)
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True, text=True
    ).stdout
    print('outputs', output)

    assert output.strip() == expected_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# read expected in/out for test fail login
expected_in2 = open(current_folder.joinpath(
    'test_login_fail.in'))
expected_out2 = open(current_folder.joinpath(
    'test_login_fail.out')).read()

# Black Box testing method: Input partitioning
# R2-2 login function should check if the supplied
# inputs meet the same email/password requirements
# login failed and compare output to expected output
# R1-4 Password has at least one special character


def test_login_fail():
    os.chdir(qbay1)
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in2,
        capture_output=True, text=True
    ).stdout
    print('outputs', output)

    assert output.strip() == expected_out2.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# read expected in/out for test fail login
empty_in = open(current_folder.joinpath(
    'test_login_empty.in'))
empty_out = open(current_folder.joinpath(
    'test_login_empty.out')).read()

# Black Box testing method: Input partitioning
# R2-2 Login function meet email/password requirement
# R1-1 Both email and password cannot be empty
# input empty email and password should failed to login


def test_login_empty():
    os.chdir(qbay1)
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=empty_in,
        capture_output=True, text=True
    ).stdout
    print('outputs', output)
    assert output.strip() == empty_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
email_long_in = open(current_folder.joinpath(
    'test_login_email_long.in'))
email_long_out = open(current_folder.joinpath(
    'test_login_email_long.out')).read()

# Black Box testing method: Input partitioning
# R2-2 Login function meet email/password requirement
# R1-3: The email has follow requirement
# email cannot be too long
# R1-4: Password minimum length 6
# input short password and too long email login will failed


def test_login_email_long():
    os.chdir(qbay1)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=email_long_in,
        capture_output=True, text=True
    ).stdout
    print('outputs', output)
    assert output.strip() == email_long_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
no_cap_in = open(current_folder.joinpath(
    'test_login_no_cap.in'))
no_cap_out = open(current_folder.joinpath(
    'test_login_no_cap.out')).read()

# Black Box testing method: Input partitioning
# R2-2 Login function meet email/password requirement
# R1-3: Email can not have underscore after at sign
# R1-4: Password has at least one uppercase
# Input password with no capital letter
# email have underscore after at
# Output: failed login with error message


def test_login_no_cap():
    os.chdir(qbay1)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=no_cap_in,
        capture_output=True, text=True
    ).stdout
    print('outputs', output)
    assert output.strip() == no_cap_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


# read expected in/out
all_cap_in = open(current_folder.joinpath(
    'test_login_all_cap.in'))
all_cap_out = open(current_folder.joinpath(
    'test_login_all_cap.out')).read()

# Black Box testing method: Input partitioning
# R2-2 Login function meet email/password requirement
# R1-4: Password has at least one lowercase
# Input: Password has all capital letters while login
# Output: failed login with error message


def test_login_all_cap():
    os.chdir(qbay1)
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=all_cap_in,
        capture_output=True, text=True
    ).stdout
    print('outputs', output)
    assert output.strip() == all_cap_out.strip()
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()
