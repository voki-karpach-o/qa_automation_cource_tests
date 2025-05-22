class TestMemoPlus:
    def test_memo_plus_positive(self, calculator_new):
        calculator_new.memo_plus(5)
        assert calculator_new.memory == [5], f'Ожидал 5 и результат {calculator_new.memory}'
