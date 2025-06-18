from qa_automation_cource.new_calc import NewCalc


class TestTopMemory:
    def test_top_memory_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        current_result = calc.top_memory
        expected_result = 5
        assert current_result == expected_result, f"Неправильное значение для верхнего значения в памяти, ожидал {expected_result} а результат {current_result}"

    def test_top_memory_negative(self):
        calc = NewCalc()
        current_result = calc.top_memory
        expected_result = 'Список пуст!'
        assert current_result == expected_result, f"Ожидал, что будет {expected_result} а результат {current_result}"
