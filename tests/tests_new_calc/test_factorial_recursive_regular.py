import pytest

from qa_automation_cource.new_calc import factorial_recursive, factorial_regular


class TestRecursive:
    def test_factorial_recursive_positive(self):
        current_result = factorial_recursive(5)
        expected_result = 120
        assert current_result == expected_result, f'Неправильное значение для факториала {factorial_recursive}, ожидал {expected_result}'

    # Проверяем, что при слишком большом числе (2500) произойдёт ошибка переполнения стека рекурсии
    def test_factorial_recursive_negative(self):
        with pytest.raises(RecursionError, match="Переполнен стек рекурсии"):
            factorial_recursive(2500)


class TestRegular:
    def test_factorial_regular_positive(self):
        current_result = factorial_regular(4)
        expected_result = 24
        assert current_result == expected_result, f'Неправильное значение для факториала {factorial_recursive}, ожидал {expected_result}'

    def test_factorial_regular_negative(self):
        with pytest.raises(RecursionError, match="Введено значение вместо числа"):
            factorial_regular('a')
