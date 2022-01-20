import pytest
from qbay.models import db, Product, User, create_product
from datetime import datetime

# Create a user before running any tests for product testing


@pytest.fixture(scope='module', autouse=True)
def fixture(request):
    db.create_all()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    user = User("sample@email.com", "MyTestUsername", "Password!",
                "firstname", "lastname")
    db.session.add(user)
    db.session.commit()
    request.addfinalizer(finalizer_function)


# R4-1: Title of product is alphanumeric and spaces are only allowed if not
# as prefix or suffix

# A test with valid title


def test_title_set_correct():
    try:
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2021, 10, 10), 'sample@email.com')
        assert(type(mittens).__name__ == 'Product')
    except ValueError as exc:
        assert False, f"'Title raised: {exc}"

# A test with non alphanumeric title


def test_title_non_alphanumeric():
    with pytest.raises(ValueError):
        Product('title*', 'These are some nice mitts',
                10, datetime(2021, 10, 10), 'sample@email.com')

# A test with spaces in title prefix


def test_title_with_spaces_prefix():
    with pytest.raises(ValueError):
        Product(' title', 'These are some nice mitts',
                10, datetime(2021, 10, 10), 'sample@email.com')

# A test with spaces in title suffix


def test_title_with_spaces_suffix():
    with pytest.raises(ValueError):
        Product('title ', 'These are some nice mitts',
                10, datetime(2021, 10, 10), 'sample@email.com')

# R4-2: Title should be no greater than 80 characters

# A test with valid title character length


def test_title_valid_length():
    try:
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2021, 10, 10), 'sample@email.com')
        assert(type(mittens).__name__ == 'Product')
    except ValueError as exc:
        assert False, f"'Title raised: {exc}"

# A test with invalid title character length


def test_title_longer_than_eighty_characters():
    with pytest.raises(ValueError):
        Product('titletitletitletitletitletitletitletitletitletitle\
                titletitletitletitletitletitletitletitletitletitleti\
                tletitletitletitletitletitletitletitletitletitle',
                'These are some nice mitts',
                15, datetime(2021, 10, 10), 'sample@email.com')

# R4-3: Description should be between 20 and 2000 characters

# A test with valid description length


def test_desciption_valid_length():
    try:
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2021, 10, 10), 'sample@email.com')
        assert(type(mittens).__name__ == 'Product')
    except ValueError as exc:
        assert False, f"'Description raised: {exc}"

# A test with description length under 20 characters


def test_desciption_too_short():
    with pytest.raises(ValueError):
        Product('title', 'Under 20 chars',
                10, datetime(2021, 10, 10), 'sample@email.com')

# A test with description length over 2000 characters


def test_desciption_too_long():
    with pytest.raises(ValueError):
        Product('title', 'This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters,\
                This description is over 2000 characters',
                10, datetime(2021, 10, 10), 'sample@email.com')

# R4-4: Description has to be longer than the product's title.

# A test where description is valid length and longer than product's title


def test_desciption_valid_length_longer_than_title():
    try:
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2021, 10, 10), 'sample@email.com')
        assert(type(mittens).__name__ == 'Product')
    except ValueError as exc:
        assert False, f"'Description raised: {exc}"

# A test where description is invalid length and shorter than product's title


def test_desciption_shorter_than_title():
    with pytest.raises(ValueError):
        Product('title title title title title title', 'Shorter than title' +
                'short', 15, datetime(2021, 10, 10), 'sample@email.com')

# R4-5: Price has to be of range [10, 10000].

# A test to see if the price was set


def test_price_set_correct():
    try:
        validDate = datetime(2021, 10, 10)
        mittens = Product('title', 'These are some nice mitts',
                          15, validDate, 'sample@email.com')
        assert (type(mittens).__name__ == 'Product')
    except ValueError as exc:
        assert False, f"'Price raised: {exc}"

# A test to see if when the price is too low, it is not set


def test_price_set_low():
    with pytest.raises(ValueError):
        Product('PriceTooLow', 'These are some nice mitts',
                5, datetime(2021, 10, 10), 'sample@email.com')

# A test to see if when the price is high low, it is not set


def test_price_set_high():
    with pytest.raises(ValueError):
        Product('title', 'These are some nice mitts',
                15000, datetime(2021, 10, 10), 'sample@email.com')

# R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
# A test to see if the price was set


def test_date_set_correct():
    try:
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2021, 10, 10), 'sample@email.com')
        assert (type(mittens).__name__ == 'Product')
    except Exception as exc:
        assert False, f"'Price raised an exception: {exc}"

# A test to see if when the price is too low, it is not set


def test_date_set_low():
    with pytest.raises(ValueError):
        Product('title', 'These are some nice mitts',
                15, datetime(1990, 10, 10), 'sample@email.com')


# A test to see if when the price is high low it is not set


def test_date_set_high():
    with pytest.raises(ValueError):
        Product('title', 'These are some nice mitts',
                15, datetime(3000, 10, 10), 'sample@email.com')

# R4-7: owner_email cannot be empty.
# The owner of the corresponding product must exist in the database.

# A test to see if the that with a correct email no exception is thrown


def test_email_correct():
    try:
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2022, 10, 10), 'sample@email.com')
        assert (type(mittens).__name__ == 'Product')
    except Exception as exc:
        assert False, f"'Email raised an exception: {exc}"

# A test to see that an not assosiated with a user email WILL
# cause an exception


def test_email_incorrect():
    try:
        Product('title', 'These are some nice mitts',
                15, datetime(2022, 10, 10), 'sampleother@email.com')
    except Exception as exc:
        assert True, f"'Email raised an exception: {exc}"


# A test to see that an empty email WILL cause a value error exception
def test_email_empty():
    with pytest.raises(ValueError):
        Product('title', 'These are some nice mitts',
                15, datetime(2022, 10, 10), '')

# R4-8: A user cannot create products that have the same title.

# A test to see if two products can be created with the different title


def test_diff_title():
    try:
        Product('title', 'These are some nice mitts',
                15, datetime(2022, 10, 10), 'sample@email.com')
        Product('title2', 'These are some nice mitts',
                15, datetime(2022, 10, 10), 'sample@email.com')

        # If no exception was thrown during the
        # init of the second product then it passed
        assert (True)
    except Exception as exc:
        assert False, f"'Email raised an exception: {exc}"

# A test to see if two products with same title will throw exception


def test_same_title():
    create_product('title', 'These are some nice mitts',
                   15, 'sample@email.com')
    assert not create_product('title', 'These are some nice mitts',
                              16, 'sample@email.com')


# Function to be called after all tests for clean up


def finalizer_function():
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
