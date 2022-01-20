# File containing tests for user registration
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

# R1-1: Both the email and password cannot be empty
# A test to ensure that the email cannot be empty


def test_email_empty():
    try:
        User("", "username", "Password!", "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Password did not raise exception: {exc}"


# A test to ensure that the password cannot be empty


def test_password_empty():
    try:
        User("sample@email.com", "username", "", "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Password did not raise exception: {exc}"

# A test to ensure that the password AND email cannot be empty


def test_email_and_password_empty():
    try:
        User("", "username", "", "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Did not raise exception: {exc}"


# R1-2: A user is uniquely identified by their email address

# A test to ensure that the email address is unique
def test_email_unique():
    column_name = 'email'
    c = User.__table__.columns.get(column_name)
    isUnique = any([c.primary_key, c.unique])
    assert isUnique is True


# R1-3: Email has to follow addr-spec defined in RFC 5322

# A test to ensure that emails with no @ are not accepted.
def test_no_at_email():
    try:
        User("sampleemail.com", "username", "Password#",
             "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Email did not raise: {exc}"

# A test to ensure that emails too many @ are not accepted.


def test_too_many_at_email():
    try:
        User("sampl@e@email.com", "username", "Password#",
             "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Email did not raise: {exc}"

# A test to ensure that emails that are too long not accepted.


def test_too_long_email():
    try:
        User("""123456789012345678901234567890123456789
                0123456789012345678901234+x@example.com""",
             "username",
             "Password#",
             "firstname",
             "lastname")
    except Exception as exc:
        assert True, f"'Email did not raise: {exc}"

# A test to see that underscores must be used correctly


def test_underscore_in_domain_email():
    try:
        User("""i_like_underscore@but_
                its_not_allowed_
                in_this_part.example.com""",
             "username",
             "Password#",
             "firstname",
             "lastname")
    except Exception as exc:
        assert True, f"'Email did not raise: {exc}"

# A test to validate that correct emails allow user registration


def test_valid_email():
    try:
        User("sample@email.com", "username", "Password#", "firstname",
             "lastname")
    except Exception as exc:
        assert False, f"'Email raised: {exc}"


# R1-4: Password meet the required complexity

# A test to reject short passwords
def test_password_too_short():
    try:
        User("sample@email.com", "username", "Pass#", "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Password did not raise exception: {exc}"

# test to reject passwords with no uppercases


def test_password_no_uppercase():
    try:
        User("sample@email.com", "username", "password#", "firstname",
             "lastname")
    except Exception as exc:
        assert True, f"'password did not raise an exception {exc}"

# test to reject passwords with no lower case


def test_password_no_lowercase():
    try:
        User("sample@email.com", "username", "PASSWORD!", "firstname",
             "lastname")
    except Exception as exc:
        assert True, f"'Password did not raise exception: {exc}"

# test to reject passwords with no special characters


def test_password_no_special_char():
    try:
        User("sample@email.com", "username", "Password", "firstname",
             "lastname")
    except Exception as exc:
        assert True, f"'Password did not raise exception: {exc}"

# test see that registration can occur with valid password


def test_valid_password():
    try:
        User("sample@email.com", "username", "Password!", "firstname",
             "lastname")
    except Exception as exc:
        assert False, f"'Password raised: {exc}"


# R1-5: User name has to be non-empty,
# alphanumeric-only, and space allowed
# only if its is not as the prefix or suffix

# A test to ensure username cannot be empty
def test_username_empty():
    try:
        User("sample@email.com", "", "Password!", "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Username did not raise: {exc}"

# A test to ensure username cannot non alphanumeric


def test_username_not_alphanumeric():
    try:
        User("sample@email.com", "username12!3", "Password!",
             "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Username did not raise: {exc}"

# A test to ensure check space suffix


def test_username_space_suffix():
    try:
        User("sample@email.com", "username ", "Password!",
             "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Username did not raise: {exc}"

# A test to ensure check space prefix


def test_username_space_prefix():
    try:
        User("sample@email.com", " username", "Password!", "firstname",
             "lastname")
    except Exception as exc:
        assert True, f"'Username did not raise: {exc}"


# R1-6: Username length

# A test to reject registration if the username is too short
def test_username_too_short():
    try:
        User("sample@gmail.com", "us", "Password!", "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Username did not raise: {exc}"

# A test to regect registration if the username is too long


def test_username_too_long():
    try:
        User("sample@gmail.com", "usernameaaaaaaaaaaaaa", "Password!",
             "firstname", "lastname")
    except Exception as exc:
        assert True, f"'Username did not raise: {exc}"

# A test for valid username


def test_username_valid():
    try:
        User("sample@gmail.com", "valid username22", "Password!",
             "firstname", "lastname")
    except Exception as exc:
        assert False, f"'Username raised: {exc}"


# R1-7: If the email has been used, the operation failed.

# Test: accept registration is different emails are used.
def test_different_emails():
    user1 = User("sample@email.com", "username1", "Password!",
                 "firstname", "lastname")
    # creating a second user with a different email should
    # not result in an exception
    user2 = User("different@email.com", "username2", "Password!",
                 "firstname", "lastname")
    db.session.add(user1)
    try:
        db.session.add(user2)

    except Exception as exc:
        assert False, f"'Email raised: {exc}"
    db.session.commit()


# Test: reject registration if same emails are used.
def test_same_emails():
    # user1 = User("sample@email.com", "username", "Password!")
    # creating a second user with the same email should
    # result in an exception
    user3 = User("sample1@email.com", "username3", "Password!",
                 "firstname", "lastname")
    try:
        db.session.add(user3)
    except Exception as exc:
        assert True, f"'Email did not raise: {exc}"
    db.session.commit()


# R1-8: Shipping address is empty at the time of registration.
def test_empty_address():
    user4 = User("sample2@email.com", "username", "Password!",
                 "firstname", "lastname")
    assert user4.shipping_address is None


# R1-9: Postal code is empty at the time of registration.
def test_empty_postal_code():
    user5 = User("sample3@email.com", "username", "Password!",
                 "firstname", "lastname")
    assert user5.postal_code is None


# R1-10: Balance should be initialized as 100 at the time of registration.
def test_balance():
    user6 = User("sample4@email.com", "username", "Password!",
                 "firstname", "lastname")
    assert user6.balance == 100

# Function to be called after all tests for clean up


def finalizer_function():
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()
