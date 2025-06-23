import pytest

divide_test_data = [
    (2, 2, 1.0),
    (-4, -1, 4.0),
    (5, 0, 0)  # так как при неправильном деление заменяем ассерт на 0,
]


@pytest.fixture(params=divide_test_data)
def divide_fixture(request):
    return request.param


class TestDivide:
    def test_divide_with_fixture_params(self, calculator_basic, divide_fixture):
        first_num, second_num, expected_result = divide_fixture
        current_result = calculator_basic.calc_divide(first_num, second_num)
        assert current_result == pytest.approx(expected_result), f'Деление чисел на валидные и не валидные значения'
