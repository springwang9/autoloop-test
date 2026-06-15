# Test case for the incorrect power() function in calculator.py
from calculator import power

def test_power_function():
    assert power(2, 10) == 1024
    assert power(3, 3) == 27
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
