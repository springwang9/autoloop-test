"""Simple calculator module."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exp):
    return base ** exp


def average(numbers):
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
