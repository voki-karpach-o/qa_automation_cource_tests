from qa_automation_cource.basic_calc import BasicCalc


class TestDivide:
    def test_divide(self):
        result = BasicCalc.calc_divide(9, 3)
        assert result == 3
