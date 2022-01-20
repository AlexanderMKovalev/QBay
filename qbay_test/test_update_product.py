import pytest
from qbay.models import Product, User, db
from datetime import datetime
# Create a user before running any tests for product testing


@pytest.fixture(scope='module', autouse=True)
def fixture(request):
    db.create_all()
    db.session.query(User).delete()
    user = User("sample@email.com", "MyTestUsername", "Password!",
                "firstname", "lastname")
    db.session.add(user)
    db.session.commit()
    request.addfinalizer(finalizer_function)


# R5-1: One can update all attributes of the product, except owner_email
# and last_modified_date.

# A test to update all of the attributes except owner_email and
# last_modified_date


def test_update_product():
    mittens = Product('title', 'These are some nice mitts',
                      10, datetime(2021, 10, 10), 'sample@email.com')
    mittens.update('newTitle', 'Oh look another decription', 500)
    assert(mittens.title == 'newTitle'
           and mittens.description == 'Oh look another decription'
           and mittens.price == 500)

# R5-2: Price can be only increased but cannot be decreased :)

# A test to update the price of product sucessfully


def test_price_increased():
    mittens = Product('title', 'These are some nice mitts',
                      15, datetime(2021, 5, 5), 'sample@email.com')
    mittens.update('title', 'Oh look another decription', 20)
    assert (type(mittens).__name__ == 'Product')

# A test to try and update the price of product unsucessfully, price is
# decreased not increased


def test_price_decreased():
    with pytest.raises(ValueError):
        mittens = Product('title', 'These are some nice mitts',
                          15, datetime(2021, 5, 5), 'sample@email.com')
        mittens.update('title', 'Oh look another decription', 11)


# R5-3: last_modified_date should be updated when the update operation is
# successful.

# A test to see if the last_modified_date was updated when the operation was
# a success


def test_date_updated():
    mittens = Product('title', 'These are some nice mitts',
                      10, datetime(2021, 10, 10), 'sample@email.com')
    mittens.update('newTitle', 'Oh look another decription', 500)
    assert(mittens.last_modified_date == datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0))

# A test to see if the last_modified_date was Not updated and an exception was
# thrown


def test_date_no_update():
    mittens = Product('title', 'These are some nice mitts',
                      10, datetime(2021, 5, 5), 'sample@email.com')
    mittens.update('Coolmittens', 'Oh look another decription', 10)
    assert (mittens.last_modified_date != datetime(2021, 5, 5))


# R5-4: When updating an attribute, one has to make sure that it follows the
# same requirements as above.

# A test to see if all the attributes are changed that they stil follow the
# same requirements.


def test_update_attributes():
    mittens = Product('title', 'These are some nice mitts',
                      10, datetime(2021, 10, 10), 'sample@email.com')
    mittens.update('newTitle', 'Oh look another decription', 500)
    assert(mittens.title == 'newTitle'
           and mittens.description == 'Oh look another decription'
           and mittens.price == 500)


# Function to be called after all tests for clean up


def finalizer_function():
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
