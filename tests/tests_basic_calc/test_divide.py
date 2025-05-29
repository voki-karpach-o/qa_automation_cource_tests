import pytest

from qa_automation_cource.basic_calc import BasicCalc

'''Почему выбрал функцию деления:
1.  Большое разнообразие на первый взгляд странных входных данных
2.  Одна из важных базовых функций которая должна работать правильно
3.  Важный момент, это проверка специфического кейса при делении на 0   
'''


@pytest.mark.critical
@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 2, 0.5),
        (0, 0, 0),
        (-1, -1, 1),
        (6, 2, 3)
    ]
)
class TestDivide:
    def test_divide_positive(self, a, b, result):
        assert BasicCalc.calc_divide(a, b) == result

    def test_divide_negative(self):
        result = BasicCalc.calc_divide(10, 0)
        assert result == 0
