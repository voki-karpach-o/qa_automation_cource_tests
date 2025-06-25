import pytest

from qa_automation_cource.new_calc import factorial_recursive, factorial_regular


class TestRecursive:
    def test_factorial_recursive_positive(self):
        current_result = factorial_recursive(5)
        expected_result = 120
        assert current_result == expected_result, (f'Позитивный кейс: вычисление рекурсивного факториала для числа '
                                                   f' {current_result}')

    def test_factorial_recursive_negative(self):
        """
            Проверяем, что рекурсивный факториал падает с RecursionError
            при попытке вычислить значение для слишком большого числа.
        """
        with pytest.raises(RecursionError):
            factorial_recursive(2500)


class TestRegular:
    def test_factorial_regular_positive(self):
        current_result = factorial_regular(4)
        expected_result = 24
        assert current_result == expected_result, (f'Негативный кейс: вычисление рекурсивного факториала для числа'
                                                   f'  {current_result}')

    def test_factorial_regular_negative(self):
        """
            Проверяем, что рекурсивный факториал падает с TypeError
            при попытке вычислить значение для буквы.
        """
        with pytest.raises(TypeError):
            factorial_regular('a')
