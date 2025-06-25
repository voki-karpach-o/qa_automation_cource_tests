import pytest


@pytest.mark.critical
class TestAdd:
    def test_add_positive(self, calculator_basic):
        current_result = calculator_basic.calc_add(5, 3)
        expected_result = 8
        assert current_result == expected_result, f'Неправильное значение для сложения {current_result}, ожидал {expected_result}'

    def test_add_negative(self, calculator_basic):
        with pytest.raises(TypeError):
            calculator_basic.calc_add('A', 3)
