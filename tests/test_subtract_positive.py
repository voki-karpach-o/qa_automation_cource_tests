import pytest

from qa_automation_cource.basic_calc import BasicCalc


class TestMultiply:
    def test_subtract(self):
        with pytest.raises(ZeroDivisionError):
            BasicCalc.calc_subtract(0, 0)
