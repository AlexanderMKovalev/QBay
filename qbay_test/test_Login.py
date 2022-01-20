# File containing tests for the login
import pytest
from qbay.models import User
from qbay.models import db
# Create a user before running any tests for product testing


@pytest.fixture(scope='module', autouse=True)
def fixture(request):
    db.create_all()
    db.session.query(User).delete()
    db.session.commit()
    request.addfinalizer(finalizer_function)

# R2-1: A user can log in using her/his email address and the password.
# R2-2: The login function should check if the supplied inputs
# meet the same email/password requirements, before checking the database
# Most of the test is in test_Register.py

# A test to see that you cannot login with just your username


def test_email_and_password_empty():
    user1 = User("sample9@email.com", "username1", "Password!",
                 "firstname", "lastname")
    db.session.add(user1)
    db.session.commit()
    try:
        user1.login("", "username1", "")
    except Exception as exc:
        assert True, f"'empty email and password not raise exception: {exc}"
    User.query.filter(User.email == "sample9@email.com").delete()

# A test to see that you cannont login with just your password


def test_param():
    user2 = User("sample2@email.com", "username2", "Password!",
                 "firstname", "lastname")
    db.session.add(user2)
    db.session.commit()
    try:
        user2.login("Password!")
    except Exception as exc:
        assert True, f"'Not enough parameter did not raise: {exc}"
    User.query.filter(User.email == "sample2@email.com").delete()

# A test to see that you cannont login with an incorrect parameter


def test_incorrect_param():
    user3 = User("sample3@email.com", "username3", "Password!",
                 "firstname", "lastname")
    db.session.add(user3)
    db.session.commit()
    try:
        user3.login("username")
    except Exception as exc:
        assert True, f"'incorrect parameter did not raise: {exc}"
    User.query.filter(User.email == "sample3@email.com").delete()

# Function to be called after all tests for clean up


def finalizer_function():
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()
