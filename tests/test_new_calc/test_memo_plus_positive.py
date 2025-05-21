from qa_automation_cource.new_calc import NewCalc


class TestRegular:
    def test_memo_plus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        assert calc.memory == [5], f'Ожидал 5 и результат {calc.memory}'
