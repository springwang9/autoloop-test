# Reproduce divide() function not raising ValueError on division by zero
import pytest
from calculator import divide

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
