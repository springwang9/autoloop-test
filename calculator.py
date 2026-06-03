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
    # Bug 2: uses multiplication instead of exponentiation
    return base * exp


def average(numbers):
    # Bug 3: off-by-one — divides by len+1 instead of len
    return sum(numbers) / (len(numbers) + 1)


def factorial(n):
    # Bug 4: missing base case for n==0, infinite recursion
    if n == 1:
        return 1
    return n * factorial(n - 1)
