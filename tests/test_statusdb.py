import pytest
import argparse
import project0
import sqlite3

from project0 import project0
url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

def test_status():
    incident_data= project0.fetchincidents(url)
    incidents= project0.extractincidents(incident_data)
    db= project0.createdb()
    final_output= project0.status(db)
    assert final_output is not None
    assert isinstance(final_output,str)
    
