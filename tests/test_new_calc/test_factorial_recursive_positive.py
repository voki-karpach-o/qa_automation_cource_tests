from qa_automation_cource.new_calc import factorial_recursive


class TestRecursive:
    def test_factorial_recursive_positive(self):
        result = factorial_recursive(5)
        assert result == 120, f'Ожидал 120, но результат {result}'
