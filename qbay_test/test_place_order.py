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
    user = User("owner@email.com", "MyTestUsername", "Password!",
                "owner", "lastname")
    user2 = User("sample@email.com", "username1", "Password!",
                 "firstname", "lastname")
    db.session.add(user)
    db.session.add(user2)
    db.session.commit()
    request.addfinalizer(finalizer_function)


# R1: A user can place an order on the products
def test_valid_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        place_an_order("Mittens", "sample@email.com", 100)
    except Exception as exc:
        assert False, f"'Should not raise: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# too many attributes should raise exception
def test_too_many_attribute_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        place_an_order("Mittens", "sample@email.com", 100, "extraAttribute")
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# too few attributes should raise exception
def test_too_few_attribute_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        place_an_order("Mittens", "sample@email.com")
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# Title
# empty title should raise exception
def test_title_empty_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("", "sample@email.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()

# title for nonexistant item should raise exception


def test_title_not_exist_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Hat", "sample@email.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid title should raise exception
def test_title_not_alphanumeric_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("!@#", "sample@email.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid title should raise exception
def test_title_too_long_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("""verrrrryyyyyyyyyyyylonggggggggggggggg
                                titleeeeeeeeeeeeeeeeeee""",
                               "sample@email.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid title should raise exception
def test_title_space_prefix_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("   Mittens", "sample@email.com",
                               100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid title should raise exception
def test_title_space_suffix_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10),
                      'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens  ", "sample@email.com",
                               100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# Email
# empty email should raise exception
def test_email_empty_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# email that isnt registered should raise exception
def test_email_no_user_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "new@email.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid email should raise exception
def test_email_no_at_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "sampleemail.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid email should raise exception
def test_email_extra_at_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "sample@@email.com",
                               100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid email should raise exception
def test_email_too_long_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", """12345678901234567890123456
                                78901234567890123456789012345678901234
                                +x@example.com""", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# invalid email should raise exception
def test_email_underscore_in_domain_order():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", """i_like_underscore@but_its_
                                not_allowed_in_this_part.example.com""",
                               100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# Balance
# negative balance should raise exception
def test_bal_negative():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "sample@email.com",
                               -100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# balance not a number should raise exception
def test_bal_not_number():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "sample@email.com",
                               "abc") is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# R2: A user cannot place an order for his/her products
def test_email_equals_owner():
    mittens = Product('Mittens', 'These are some nice mitts',
                      15, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "owner@email.com", 100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


# R3: A user cannot place an order that costs more than his/her balance
def test_bal_less_price():
    mittens = Product('Mittens', 'These are some nice mitts',
                      150, datetime(2021, 10, 10), 'owner@email.com')
    db.session.add(mittens)
    try:
        assert (place_an_order("Mittens", "sample@email.com",
                               100) is not False)
    except Exception as exc:
        assert True, f"'Should raise exception: {exc}"
    db.session.query(Product).delete()
    db.session.commit()


def finalizer_function():
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()
    db.session.close()
