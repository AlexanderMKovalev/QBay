
import os
SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
This file defines what to do BEFORE running any test cases:
'''


def pytest_sessionstart():
    '''
    Delete database file if existed. So testing can start fresh.
    '''
    print('Setting up environment..')
    db_file = 'db.sqlite'
    if os.path.exists(db_file):
        os.remove(db_file)


def pytest_sessionfinish():
    '''
    Optional function called when testing is done.
    Do nothing for now
    '''
    pass
