class TestTopMemory:
    def test_top_memory_positive(self, calculator_new):
        calc = calculator_new()
        calc.memo_plus(5)
        current_result = calc.top_memory
        expected_result = 5
        assert current_result == expected_result, f"Неправильное значение для верхнего значения в памяти, ожидал {expected_result} а результат {current_result}"

    def test_top_memory_negative(self, calculator_new):
        calc = calculator_new
        current_result = calc.top_memory
        expected_result = 'Список пуст!'
        assert current_result == expected_result, f"Ожидал, что будет {expected_result} а результат {current_result}"
