import pytest
import function_with_bug_subtract


@pytest.mark.xfail(reason="Баг в логике вычитания")
def test_add():
    result = function_with_bug_subtract.calc_subtract(5, 3)
    assert result == 2
