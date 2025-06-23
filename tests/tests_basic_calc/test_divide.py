import pytest

from qa_automation_cource.basic_calc import BasicCalc

'''Почему выбрал функцию деления:
1.  Большое разнообразие на первый взгляд странных входных данных
2.  Одна из важных базовых функций которая должна работать правильно
3.  Важный момент, это проверка специфического кейса при делении на 0   
'''


@pytest.mark.critical
class TestDivide:
    @pytest.mark.parametrize(
        "a_positive, b_positive, expected_result_positive",
        [
            (1, 2, 0.5),
            (0, 0, 0),
            (-1, -1, 1),
            (6, 2, 3)
        ]
    )
    def test_divide_positive(self, a_positive, b_positive, expected_result_positive):
        calc = BasicCalc()
        current_result = calc.calc_divide(a_positive, b_positive)
        assert current_result == expected_result_positive, f'Позитивный кейс: деление на валидные значения'

    @pytest.mark.parametrize(
        "a_negative, b_negative, expected_result_negative",
        [
            (5, '3', TypeError),
            ('a', 3, TypeError),
            ('', '', TypeError),
            (-140, '', TypeError)
        ]
    )
    def test_divide_negative(self, a_negative, b_negative, expected_result_negative):
        calc = BasicCalc()
        with pytest.raises(expected_result_negative):
            calc.calc_divide(a_negative, b_negative)

    @pytest.mark.parametrize(
        "a, b, expected_result",
        [
            (100, 0, 0),
            ('c', 0, 0)
        ]
    )
    def test_divide_by_zero(self, a, b, expected_result):
        calc = BasicCalc()
        current_result = calc.calc_divide(a, b)
        assert current_result == expected_result
        assert current_result == expected_result
