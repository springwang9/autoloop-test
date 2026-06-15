import pytest
from calculator import divide

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_divide_normal():
    assert divide(10, 2) == 5.0