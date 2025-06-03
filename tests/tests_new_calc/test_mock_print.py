from qa_automation_cource.basic_calc import BasicCalc


# Провереряем, что выводится правильный текст принта, нужно для того, чтобы не вызывая код проверить только текст
def test_divide_by_zero_with_mock(mocker):
    mock_print = mocker.patch('builtins.print')

    BasicCalc.calc_divide(10, 0)

    mock_print.assert_called_with("Ошибка деления на ноль!")
