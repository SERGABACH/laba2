import pytest
from my_library import fibonacci, bubble_sort, calculator


def test_fibonacci_positive_numbers():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_zero_or_negative_numbers():
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_bubble_sort():
    arr = [8, 3, 1, 6, 2, 9, 4, 5, 7]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_calculator_addition():
    assert calculator(2, 3, '+') == 5
    assert calculator(-5, 10, '+') == 5

def test_calculator_subtraction():
    assert calculator(5, 3, '-') == 2
    assert calculator(10, -5, '-') == 15

def test_calculator_multiplication():
    assert calculator(2, 3, '*') == 6
    assert calculator(-5, -10, '*') == 50

def test_calculator_division():
    assert calculator(10, 2, '/') == 5
    assert calculator(-7, 2, '/') == -3.5

def test_calculator_zero_division():
    with pytest.raises(ZeroDivisionError):
        calculator(2, 0, '/')
        calculator(0, 0, '/')

def test_calculator_invalid_operation():
    with pytest.raises(ValueError):
        calculator(2, 3, '^')

