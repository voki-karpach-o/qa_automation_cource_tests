from qa_automation_cource.basic_calc import BasicCalc


class TestAdd:
    def test_add(self):
        result = BasicCalc.calc_add(5, 3)
        assert result == 8
