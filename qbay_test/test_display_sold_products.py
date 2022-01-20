import pytest
from qbay.models import db, Product, User, place_an_order
from datetime import datetime


# input partition
# Create a user before running any tests for place order testing
@pytest.fixture(scope='module', autouse=True)
def fixture(request):
    db.create_all()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    user = User("sample1@email.com", "username1", "Password!",
                "firstname1", "lastname3")
    user2 = User("sample2@email.com", "username2", "Password!",
                 "firstname2", "lastname3")
    user3 = User("sample3@email.com", "username3", "Password!",
                 "firstname3", "lastname3")
    db.session.add(user)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
    request.addfinalizer(finalizer_function)


# R4: A sold product will not be shown on the other user's user interface.
# Output Partioning
# A test that creates a product, sells it and tests if the buyer
# can see the sold product
# They should not
def test_sold_product_not_show():
    # Create a product for user1
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'sample1@email.com')
    db.session.add(mittens)

    # Sell mittens to user2
    place_an_order("Mittens", "sample2@email.com", 100)

    # Query sold products for user2
    all_products = Product.query.filter_by(
        sold=True, owner_email='sample2@email.com').all()

    # They should see no products
    assert (len(all_products) == 0)

    db.session.query(Product).delete()
    db.session.commit()

# R4: A sold product will not be shown on the other user's user interface.
# Output Partioning
# A test that creates a product, sells it and tests if a user who is not
# the seller can see the sold product
# They should not


def test_sold_product_not_show2():
    # Create a product for user1
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'sample1@email.com')
    db.session.add(mittens)

    # Sell mittens to user2
    place_an_order("Mittens", "sample2@email.com", 100)

    # Query sold products for user3
    all_products = Product.query.filter_by(
        sold=True, owner_email='sample3@email.com').all()

    # They should see no products
    assert (len(all_products) == 0)

    db.session.query(Product).delete()
    db.session.commit()

# R5: A sold product can be shown on the owner's user interface.
# Output Partioning
# A test that creates a product, sells it and tests if the
# seller can see they product
# They should


def test_sold_product_show():
    # Create a product for user1
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'sample1@email.com')
    db.session.add(mittens)

    # Sell mittens to user2
    place_an_order("Mittens", "sample2@email.com", 100)

    # Query sold products for user3
    all_products = Product.query.filter_by(
        sold=True, owner_email='sample1@email.com').all()

    # They should see no products
    assert (len(all_products) == 1)

    db.session.query(Product).delete()
    db.session.commit()


def finalizer_function():
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
