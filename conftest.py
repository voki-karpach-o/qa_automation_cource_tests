import sys
import os
import pytest
from qa_automation_cource.basic_calc import BasicCalc

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def calculator_basic():
    calc = BasicCalc()
    return calc
