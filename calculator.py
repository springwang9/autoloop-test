"""Simple calculator module."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Bug 1: no check for division by zero
    return a / b


def power(base, exp):
    return base ** exp


def average(numbers):
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def factorial(n):
    # Bug 4: missing base case for n==0, infinite recursion
    if n == 1:
        return 1
    return n * factorial(n - 1)
