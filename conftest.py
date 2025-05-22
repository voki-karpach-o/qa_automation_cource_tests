import sys
import os
import pytest
from qa_automation_cource.new_calc import NewCalc

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def calculator_new():
    calc = NewCalc()
    return calc
