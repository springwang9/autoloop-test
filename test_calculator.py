"""Tests for calculator module."""
import pytest
from calculator import add, subtract, multiply, divide, power, average, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide_normal():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_power():
    assert power(2, 10) == 1024
    assert power(3, 3) == 27


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10, 20]) == 15.0


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1) == 1


# Regression tests for bugs that were fixed
def test_regression_divide_by_zero():
    """Bug 1: divide() should raise ValueError, not ZeroDivisionError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_regression_power():
    """Bug 2: power() should compute exponentiation, not multiplication."""
    assert power(2, 10) == 1024
    assert power(5, 3) == 125
    assert power(10, 0) == 1


def test_regression_average():
    """Bug 3: average() should divide by len, not len+1."""
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([100]) == 100.0
    with pytest.raises(ValueError, match="Cannot average an empty list"):
        average([])


def test_regression_factorial():
    """Bug 4: factorial(0) should return 1, not infinite recursion."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(10) == 3628800
