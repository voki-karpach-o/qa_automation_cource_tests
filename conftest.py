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


@pytest.fixture
def calculator_new_with_memory():
    calc = NewCalc()
    calc.memo_plus(5)
    return calc


@pytest.fixture
def temp_log_file(tmpdir):
    log_file = tmpdir.join("calculator_log.txt")
    yield log_file
    if os.path.exists(log_file):
        os.remove(log_file)


def generate_test_data():
    test_data = [
        (1, 2, 3),  # 3
        (5, 3, 8),  # 8
        (-1, -1, -2),  # -2
        (0, 0, 0),  # 0
    ]
    return test_data


@pytest.fixture
def test_data():
    return generate_test_data()
