import pytest
import argparse
import project0
import sqlite3
from project0 import project0
url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

def test_populatedb():
    sql = sqlite3.connect(db)
    a = sql.cursor()
    a.execute('SELECT * FROM incidents')
    result = cur.fetchall()
    assert a is not None   
