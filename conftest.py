import sys
import os
from datetime import datetime

import pytest
from qa_automation_cource.basic_calc import BasicCalc
from qa_automation_cource.new_calc import NewCalc

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)


@pytest.fixture
def calculator_basic():
    calc = BasicCalc()
    return calc


@pytest.fixture
def calculator_new():
    calc = NewCalc()
    return calc


@pytest.fixture
def calculator_with_memory(calculator_new):
    calculator_new.memo_plus(5)
    return calculator_new


@pytest.fixture
def temp_log_file(tmp_path):
    log_file_path = tmp_path / "calculator_log.txt"
    return log_file_path


@pytest.fixture
def calculator_with_temp_log(monkeypatch, temp_log_file):
    def fake_log_operation(self, operation_type, arguments, result_val):
        date_logging = datetime.now().date().strftime("%Y.%m.%d")
        time_logging = datetime.now().time().strftime("%H:%M:%S")
        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result_val,
            "Дата": date_logging,
            "Время": time_logging
        }
        with open(temp_log_file, "a", encoding="utf-8") as log_file_op:
            log_file_op.write(str(log_entry) + "\n")

    monkeypatch.setattr(NewCalc, 'log_operation', fake_log_operation)

    calc = NewCalc()
    calc.test_log_file = temp_log_file
    return calc


divide_test_data = [
    (2, 2, 1.0),
    (-4, -1, 4.0),
    (5, 0, 0)  # так как при неправильном деление заменяем ассерт на 0,
]


@pytest.fixture(params=divide_test_data)
def divide_fixture(request):
    return request.param

