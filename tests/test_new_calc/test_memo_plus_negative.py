from qa_automation_cource.new_calc import NewCalc


class TestMemoPlus:
    def test_memo_plus_negative(self):
        calc = NewCalc()
        calc.memo_plus(5)
        calc.memo_plus(10)
        calc.memo_plus(15)
        calc.memo_plus(20)
        assert len(calc.memory) == 3, f'Ожидал, что добавится не больше 3 значений и результат {len(calc.memory)}'
