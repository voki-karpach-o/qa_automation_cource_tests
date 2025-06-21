class TestTopMemory:
    def test_top_memory_positive(self, calculator_with_memory):
        current_result = calculator_with_memory
        expected_result = 5
        assert current_result == expected_result, f"Неправильное значение для верхнего значения в памяти, ожидал {expected_result} а результат {current_result}"
