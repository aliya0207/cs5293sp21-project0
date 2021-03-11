import pytest
import argparse
import project0
from project0 import project0
url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

def test_status():
    incident_data= project0.fetchincidents(url)
    incidents= project0.extractincidents(incident_data)
    db= project0.createdb()
    output= project0.statusdb()
    msg= "Error. test not satisfied."
    assert output is not None
    assert isinstance(output,list,msg)
    
