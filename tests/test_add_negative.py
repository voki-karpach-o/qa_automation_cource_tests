import pytest
from qa_automation_cource.basic_calc import BasicCalc


class TestAdd:
    def test_add(self):
        with pytest.raises(TypeError):
            BasicCalc.calc_add('A', 3)
