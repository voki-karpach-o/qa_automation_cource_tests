from qa_automation_cource.basic_calc import BasicCalc


class TestAddNew:
    def test_add(self, test_data):
        for a, b, expected in test_data:
            result = BasicCalc.calc_add(a, b)
            assert result == expected, f"Ожидаю {expected} и получилось {result}"
