import pytest

from qa_automation_cource.basic_calc import BasicCalc


@pytest.mark.critical
class TestMultiply:
    def test_multiply_positive(self):
        current_result = BasicCalc.calc_multiply(2, 3)
        expected_result = 6
        assert current_result == expected_result, f'Неправильное значение для умножения {current_result}, ожидал {expected_result}'

    def test_multiply_negative(self):
        with pytest.raises(TypeError, match="Одним из значений является пустая строка"):
            BasicCalc.calc_add('', 3)
