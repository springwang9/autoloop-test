import pytest
from calculator import factorial

def test_factorial_edge_cases_and_negative_inputs():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1) == 1
    with pytest.raises(ValueError):
        factorial(-1)