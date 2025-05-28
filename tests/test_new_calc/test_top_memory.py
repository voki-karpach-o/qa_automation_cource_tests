from qa_automation_cource.new_calc import NewCalc


class TestTopMemory:
    def test_top_memory_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        result = calc.top_memory
        assert result == 5, f"Ожидаю, что будет возвращено 5 и результат {result}"

    def test_top_memory_negative(self):
        calc = NewCalc()
        result = calc.top_memory
        assert result == 'Список пуст!', f"Ожидаю, что будет 'Список пуст!' и результат {result}"
