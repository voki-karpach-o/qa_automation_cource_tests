from qa_automation_cource.new_calc import NewCalc


class TestMemoMinus:
    def test_memo_minus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        calc.memo_plus(10)
        calc.memo_minus()
        assert calc.memory == [5], f'Ожидал, что в памяти число 5 и результат {calc.memory}'

    def test_memo_minus_negative(self):
        calc = NewCalc()
        calc.memo_minus()
        assert calc.memory == [], f'Ожидал, что в памяти нет чисел и результат {calc.memory}'


class TestMemoPlus:
    def test_memo_plus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        assert calc.memory == [5], f'Ожидал 5 и результат {calc.memory}'

    def test_memo_plus_negative(self):
        calc = NewCalc()
        calc.memo_plus(5)
        calc.memo_plus(10)
        calc.memo_plus(15)
        calc.memo_plus(20)
        assert len(calc.memory) == 3, f'Ожидал, что добавится не больше 3 значений и результат {len(calc.memory)}'
