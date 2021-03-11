import pytest
import argparse
from project0 import project0
url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"
def test_createdb():
    database='normanpd.db'
    dbname = project0.createdb()
    assert dbname == database
