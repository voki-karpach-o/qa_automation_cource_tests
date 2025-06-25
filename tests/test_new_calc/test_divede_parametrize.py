import pytest


class TestDivide:
    def test_divide_with_fixture_params(self, calculator_basic, divide_fixture):
        first_num, second_num, expected_result = divide_fixture
        current_result = calculator_basic.calc_divide(first_num, second_num)
        assert current_result == pytest.approx(expected_result), f'Неправильное значение для деления {current_result}, ожидал {expected_result}'
