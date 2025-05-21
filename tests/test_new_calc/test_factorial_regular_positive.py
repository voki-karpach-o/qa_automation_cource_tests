from qa_automation_cource.new_calc import factorial_regular


class TestRegular:
    def test_factorial_regular_positive(self):
        result = factorial_regular(4)
        assert result == 24, f'Ожидал 24, но результат {result}'
