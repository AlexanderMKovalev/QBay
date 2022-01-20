from pathlib import Path
from qbay.models import User, create_user
from qbay.models import db

# Testing method: Fuzzy Testing

# get expected input/output file
current_folder = Path(__file__).parent

# Clear users from db
db.session.query(User).delete()
db.session.commit()
db.session.close()


payload = open(current_folder.joinpath(
    'payload.txt'))


def test_fuzzy_register_email():
    i = 0
    for line in payload:
        try:
            create_user(line, "testUser" + str(i),
                        "Password!", "firstname", "lastname")
            print(line)
        except Exception:
            continue
        i = i + 1

    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


def test_fuzzy_register_username():
    i = 0
    for line in payload:
        try:
            create_user(str(i) + "cfor@queensu.ca", line,
                        "Password!", "firstname", "lastname")

            print(line)
        except Exception:
            continue
        i = i + 1

    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


def test_fuzzy_register_password():
    i = 0
    for line in payload:
        try:
            create_user(str(i) + "cfor@queensu.ca", "testUser" + str(i),
                        line, "firstname", "lastname")

            print(line)
        except Exception:
            continue
        i = i + 1

    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


def test_fuzzy_register_firstname():
    i = 0
    for line in payload:
        try:
            create_user(str(i) + "cfor@queensu.ca", "testUser" + str(i),
                        "Password!", line, "lastname")
            print(line)
        except Exception:
            continue
        i = i + 1

    db.session.query(User).delete()
    db.session.commit()
    db.session.close()


def test_fuzzy_register_lastname():
    i = 0
    for line in payload:
        try:
            create_user(str(i) + "cfor@queensu.ca", "testUser" + str(i),
                        "Password!", "firstname", line)
            print(line)
        except Exception:
            continue
        i = i + 1

    db.session.query(User).delete()
    db.session.commit()
    db.session.close()
