from qa_automation_cource.basic_calc import BasicCalc


class TestAdd:
    def test_add(self):
        result = BasicCalc.calc_add('A', 3)
        assert result == TypeError, 'Нельзя вводить текст как число!'
