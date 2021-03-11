import pytest
import argparse
from project0 import project0

def test_fetchincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"
    assert project0.fetchincidents(url) is not None
