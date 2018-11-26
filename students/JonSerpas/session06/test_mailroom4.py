import os
from mailroom4 import create_report, everyone


def get_donors_db():
    donors = {'Bill Gates': [1000, 2000, 3000],
              'Rick James': [5000, 5000, 6000, 3000],
              'James Brown': [4000, 10000, 9000, 12000],
              'Prince': [5500, 6500, 7000, 12000],
              'Cat Williams': [2000, 3000, 1000]}
    return donors


def test1():
    donors = get_donors_db()
    assert len(create_report(donors)) == len(donors)


def test2():
    donors = get_donors_db()
    everyone(donors)
    for i in donors:
        assert os.path.exists(i + ".txt")
