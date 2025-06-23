class TestAdd:
    def test_top_memory_and_logging(self, calculator_with_temp_log):
        calc = calculator_with_temp_log
        calc.num_1 = "12+8"
        calc.calculate_result()
        log_content = calc.test_log_file.read_text(encoding="utf-8")
        print(f"Содержимое лога: {log_content}")
