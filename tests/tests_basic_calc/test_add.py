import pytest

from qa_automation_cource.basic_calc import BasicCalc


@pytest.mark.critical
class TestAdd:
    def test_add_positive(self):
        current_result = BasicCalc.calc_add(5, 3)
        expected_result = 8
        assert current_result == expected_result, f'Неправильное значение для сложения {current_result}, ожидал {expected_result}'

    def test_add_negative(self):
        with pytest.raises(TypeError, match="Одним из значений является строка"):
            BasicCalc.calc_add('A', 3)
