from qa_automation_cource.new_calc import NewCalc


class TestMemoMinus:
    def test_memo_minus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        calc.memo_plus(10)
        calc.memo_minus()
        assert calc.memory == [5], f'Ожидал, что в памяти число 5 и результат {calc.memory}'
