import sys
import os
import pytest
from qa_automation_cource.new_calc import NewCalc

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)


@pytest.fixture
def calculator_new():
    calc = NewCalc()
    return calc
