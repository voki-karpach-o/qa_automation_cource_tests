import pytest

from qa_automation_cource.basic_calc import BasicCalc


@pytest.mark.critical
class TestSubtract:
    def test_subtract_positive(self):
        current_result = BasicCalc.calc_subtract(5, 3)
        expected_result = 2
        assert current_result == expected_result, f'Неправильное значение для вычитания {current_result}, ожидал {expected_result}'

    def test_subtract_negative(self):
        with pytest.raises(TypeError, match="Одним из значений является строка"):
            BasicCalc.calc_subtract('A', 3)
