import pytest

from qa_automation_cource.new_calc import factorial_regular


class TestRegular:
    def test_factorial_recursive_negative(self):
        with pytest.raises(RecursionError):
            factorial_regular('a')
