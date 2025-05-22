from qa_automation_cource.new_calc import NewCalc


class TestTopMemory:
    def test_top_memory_negative(self):
        calc = NewCalc()
        result = calc.top_memory
        assert result == 'Список пуст!', f"Ожидаю, что будет 'Список пуст!' и результат {result}"
