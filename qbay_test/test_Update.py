from qbay.models import User
import pytest
from qbay.models import db
# Create a user before running any tests for product testing


@pytest.fixture(scope='module', autouse=True)
def fixture(request):
    db.create_all()
    db.session.query(User).delete()
    db.session.commit()
    request.addfinalizer(finalizer_function)


# R3-1: Cannot update other attribtues
# A test to see that the user can be updated


def test_valid_update():
    user1 = User("sample1@email.com", "username1", "Password!",
                 "firstname", "lastname")
    db.session.add(user1)
    user1.update_user_name("newusername1")
    user1.update_shipping_address("1234 Main Street")
    user1.update_postal_code("A1A 1A1")
    pytest.assume(user1.user_name == "newusername1")
    pytest.assume(user1.shipping_address == "1234 Main Street")
    pytest.assume(user1.postal_code == "A1A 1A1")


# A test too see if some other attributes are trying to be changed


def test_too_many_attributes():
    user2 = User("sample2@email.com", "username2", "Password!",
                 "firstname", "lastname")
    db.session.add(user2)
    try:
        user2.update_user_name("newusername2", "1234 Main Street", "A1A 1A1")
    except Exception as exc:
        assert True, f"'Too many attributes did not raise: {exc}"

# A test to reject updating user if attributes are incorrect


def test_incorrect_attributes():
    user3 = User("sample3@email.com", "username3", "Password!",
                 "firstname", "lastname")
    db.session.add(user3)
    try:
        user3.update_shipping_address("newusername3",
                                      "1234 Main Street", balance=100)
    except Exception as exc:
        assert True, f"'Attempt to update balance did not raise: {exc}"


# R3-2: Shipping address should meet style requirement
# Testing if address is empty, should fail

def test_address_empty():
    user4 = User("sample4@email.com", "username4", "Password!",
                 "firstname", "lastname")
    db.session.add(user4)
    try:
        user4.update_shipping_address("")
    except Exception as exc:
        assert True, f"'shipping address did not raise exception: {exc}"

# Testing is address is not alphnumeric, should fail


def test_shipping_address_not_alphanumeric():
    user5 = User("sample5@email.com", "username5", "Password!",
                 "firstname", "lastname")
    db.session.add(user5)
    try:
        user5.update_shipping_address("@@123 Kingston Street")
    except Exception as exc:
        assert True, f"'shipping address did not raise exception: {exc}"


# R3-3: Postal code has to be a valid Canadian postal code.
# Canadian postal codes follow format A1A 1A1
# where A is a letter and 1 is a number

# A test for invalid postal code, should fail
def test_invalid_format_postal_code():
    user6 = User("sampl6e@email.com", "username6", "Password!",
                 "firstname", "lastname")
    db.session.add(user6)
    # invalid postal code should fail
    # due to wrong format
    try:
        user6.update_postal_code("312 0B1")
    except Exception as exc:
        assert True, f"'Postal_code did not raise: {exc}"

# A test for invalid postal code (too short), should fail


def test_too_short_postal_code():
    user7 = User("sample7@email.com", "username7", "Password!",
                 "firstname", "lastname")
    # invalid postal code should fail
    # due to too short
    try:
        user7.update_postal_code("A1A")
    except Exception as exc:
        assert True, f"'Postal_code did not raise: {exc}"

# A test for invalid postal code (too long), should fail


def test_too_long_postal_code():
    user8 = User("sample8@email.com", "username8", "Password!",
                 "firstname", "lastname")
    db.session.add(user8)
    # invalid postal code should fail
    # due to too long
    try:
        user8.update_postal_code("K1A 0B11")
    except Exception as exc:
        assert True, f"'Postal_code did not raise: {exc}"

# A test for invalid postal code, using invalid characters


def test_invalid_char_postal_code():
    user9 = User("sample9@email.com", "username9", "Password!",
                 "firstname", "lastname")
    db.session.add(user9)
    # invalid postal code should fail
    # due to invalid character(s)
    try:
        user9.update_postal_code("K1A 0@Q")
    except Exception as exc:
        assert True, f"'Postal_code did not raise: {exc}"

# Function to be called after all tests for clean up


def finalizer_function():
    db.session.query(User).delete()
    db.session.commit()
    db.session.close()
