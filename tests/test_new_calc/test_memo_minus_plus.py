import pytest

from qa_automation_cource.new_calc import NewCalc


class TestMemoMinus:
    def test_memo_minus_positive(self):
        calc = NewCalc()
        calc.memory = [5, 10, 15]
        calc.memo_minus()
        assert calc.memory == [5, 10], "Позитивный кейс: удаление значения из памяти"

    def test_memo_minus_negative(self):
        """
            Проверяет, что memo_minus выбрасывает ValueError при попытке
            извлечь значение из пустой памяти.
        """
        calc = NewCalc()
        with pytest.raises(ValueError):
            calc.memo_minus()


class TestMemoPlus:
    def test_memo_plus_positive(self):
        calc = NewCalc()
        calc.memo_plus(5)
        current_result = calc.memory
        expected_result = [5]
        assert current_result == expected_result, f"Позитивный кейс: добавление значение в память {calc.memory}"

    def test_memo_plus_negative(self):
        calc = NewCalc()
        calc.memory = [5, 10, 15, 20]
        current_result = len(calc.memory)
        expected_result = 3
        assert current_result == expected_result, (f'Негативный кейс: превышено количество значений в памяти '
                                                   f' {calc.memory}')
