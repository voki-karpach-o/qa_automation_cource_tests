import pytest

from qa_automation_cource.new_calc import factorial_recursive, factorial_regular


class TestRecursive:
    def test_factorial_recursive_positive(self):
        result = factorial_recursive(5)
        assert result == 120, f'Ожидал 120, но результат {result}'

    def test_factorial_recursive_negative(self):
        with pytest.raises(RecursionError):
            factorial_recursive(2500)


class TestRegular:
    def test_factorial_regular_positive(self):
        result = factorial_regular(4)
        assert result == 24, f'Ожидал 24, но результат {result}'

    def test_factorial_regular_negative(self):
        with pytest.raises(RecursionError):
            factorial_regular('a')
