import pytest

from qa_automation_cource.new_calc import factorial_recursive


class TestRecursive:
    def test_factorial_recursive_negative(self):
        with pytest.raises(RecursionError):
            factorial_recursive(2500)
