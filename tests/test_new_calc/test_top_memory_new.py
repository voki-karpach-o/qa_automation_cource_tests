class TestTopMemory:
    def test_top_memory_positive(self, calculator_with_memory):
        current_result = calculator_with_memory.top_memory
        expected_result = 5
        assert current_result == expected_result, f"Неправильное значение для верхнего значения в памяти, ожидал {expected_result} а результат {current_result}"

    def test_top_memory_and_logging(self, calculator_with_temp_log):
        calc = calculator_with_temp_log
        calc.num_1 = "12+8"
        calc.calculate_result()
        log_content = calc.test_log_file.read_text(encoding="utf-8")
        print(f"Содержимое лога: {log_content}")
