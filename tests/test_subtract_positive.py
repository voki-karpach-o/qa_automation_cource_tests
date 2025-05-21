from qa_automation_cource.basic_calc import BasicCalc


class TestMultiply:
    def test_subtract(self):
        result = BasicCalc.calc_subtract(5, 3)
        assert result == 2
