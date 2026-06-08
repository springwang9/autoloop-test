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


def test_average_single_element():
    assert average([42]) == 42.0


def test_average_empty_list():
    with pytest.raises(ValueError, match="Cannot compute average of an empty list"):
        average([])


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1) == 1
