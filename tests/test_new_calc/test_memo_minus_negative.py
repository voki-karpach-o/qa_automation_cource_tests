from qa_automation_cource.new_calc import NewCalc


class TestMemoMinus:
    def test_memo_minus_negative(self):
        calc = NewCalc()
        calc.memo_minus()
        assert calc.memory == [], f'Ожидал, что в памяти нет чисел и результат {calc.memory}'
