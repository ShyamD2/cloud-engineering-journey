"""
Day 1: HackerRank Python Warmups
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Solutions for essential Python foundation exercises:
1. Say "Hello, World!" with Python
2. Python If-Else (Conditionals)
3. Arithmetic Operators
4. Python: Division
5. Loops (Square of non-negative integers)
6. Write a Function (is_leap year calculation)
"""

def hello_world() -> str:
    """Challenge 1: Say Hello, World! with Python"""
    msg = "Hello, World!"
    return msg


def python_if_else(n: int) -> str:
    """
    Challenge 2: Python If-Else
    Given an integer n, perform the following conditional actions:
    - If n is odd, print Weird
    - If n is even and in inclusive range of 2 to 5, print Not Weird
    - If n is even and in inclusive range of 6 to 20, print Weird
    - If n is even and greater than 20, print Not Weird
    """
    if n % 2 != 0:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


def arithmetic_ops(a: int, b: int) -> tuple[int, int, int]:
    """Challenge 3: Arithmetic Operators (Sum, Difference, Product)"""
    return (a + b, a - b, a * b)


def python_division(a: int, b: int) -> tuple[int, float]:
    """Challenge 4: Integer and Float Division"""
    int_div = a // b
    float_div = a / b
    return (int_div, float_div)


def python_loops(n: int) -> list[int]:
    """Challenge 5: Loops - For all non-negative integers i < n, print i^2"""
    return [i ** 2 for i in range(n)]


def is_leap(year: int) -> bool:
    """
    Challenge 6: Write a Function - Leap Year Validator
    A year is leap if:
    - divisible by 4, unless divisible by 100 (not leap) unless also divisible by 400 (leap).
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


if __name__ == "__main__":
    print("=== Testing HackerRank Python Warmups ===")
    assert hello_world() == "Hello, World!"
    assert python_if_else(3) == "Weird"
    assert python_if_else(4) == "Not Weird"
    assert python_if_else(18) == "Weird"
    assert python_if_else(24) == "Not Weird"
    assert arithmetic_ops(3, 2) == (5, 1, 6)
    assert python_division(4, 3) == (1, 4 / 3)
    assert python_loops(5) == [0, 1, 4, 9, 16]
    assert is_leap(2000) is True
    assert is_leap(2100) is False
    assert is_leap(2024) is True
    print("[PASS] All HackerRank Python warmup tests passed successfully!")
