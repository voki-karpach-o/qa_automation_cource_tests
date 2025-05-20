from qa_automation_cource.basic_calc import BasicCalc


class TestMultiply:
    def test_multiply(self):
        result = BasicCalc.calc_multiply('', 3)
        assert result == '', "Умножение пустой строки на число вернёт пустую строку"