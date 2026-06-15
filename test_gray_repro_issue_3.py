# average() function off-by-one error reproduction
from calculator import average

def test_average_off_by_one_error():
    numbers = [1, 2, 3, 4, 5]
    expected_average = sum(numbers) / len(numbers)
    assert average(numbers) == expected_average
