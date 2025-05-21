from qa_automation_cource.basic_calc import BasicCalc


class TestSubtract:
    def test_subtract(self):
        result = BasicCalc.calc_subtract(0, 0)
        assert result == 0, 'Введите другие значения'
