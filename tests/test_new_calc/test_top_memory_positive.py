class TestTopMemory:
    def test_top_memory_positive(self, calculator_new_with_memory):
        result = calculator_new_with_memory.top_memory
        assert result == 5, f"Ожидаю, что будет возвращено 5 и результат {result}"
