from qa_automation_cource.new_calc import NewCalc


class TestMemoMinus:
    def test_memo_minus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        calc.memo_plus(10)
        calc.memo_minus()
        current_result = calc.memory
        expected_result = [5]
        assert current_result == expected_result, f"Неправильное значение для верхнего значения в памяти, ожидал {expected_result} а результат {current_result}"

    def test_memo_minus_negative(self):
        calc = NewCalc()
        calc.memo_minus()
        current_result = calc.memory
        expected_result = []
        assert current_result == expected_result, f'Ожидал, что в памяти нет чисел a результат {current_result}'


class TestMemoPlus:
    def test_memo_plus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        current_result = calc.memory
        expected_result = [5]
        assert current_result == expected_result, f"Неправильное значение для верхнего значения в памяти, ожидал {expected_result} а результат {current_result}"

    def test_memo_plus_negative(self):
        calc = NewCalc()
        calc.memo_plus(5)
        calc.memo_plus(10)
        calc.memo_plus(15)
        calc.memo_plus(20)
        current_result = len(calc.memory)
        expected_result = 3
        assert current_result == expected_result, f'Ожидал, что добавится не больше 3 значений а добавилось {current_result}'
