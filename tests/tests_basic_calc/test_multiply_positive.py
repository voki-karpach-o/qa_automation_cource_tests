import pytest

from qa_automation_cource.basic_calc import BasicCalc


@pytest.mark.critical
class TestMultiply:
    def test_multiply(self):
        result = BasicCalc.calc_multiply(2, 3)
        assert result == 6
