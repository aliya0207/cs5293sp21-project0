import pytest
import argparse
import project0
from project0 import project0
url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

def test_extract_incidents():
    project0.fetchincidents(url)
    l = project0.extractincidents()
    assert len(l) > 0
