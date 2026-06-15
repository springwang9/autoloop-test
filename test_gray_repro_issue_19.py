# Test factorial function for correct handling of edge cases and negative inputs
import calculator
import pytest

def test_factorial_edge_cases_and_negative_inputs():
    assert calculator.factorial(0) == 1
    assert calculator.factorial(5) == 120
    assert calculator.factorial(1) == 1
    with pytest.raises(ValueError):
        calculator.factorial(-1)
