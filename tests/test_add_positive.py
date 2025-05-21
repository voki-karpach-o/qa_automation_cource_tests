from qa_automation_cource.basic_calc import BasicCalc


class TestMultiply:
    def test_subtract(self):
        result = BasicCalc.calc_add(5, 3)
        assert result == 8
