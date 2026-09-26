"""
Day 6: Basic DSA — LeetCode #20: Valid Parentheses
Script: leetcode_20_valid_parentheses.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from __future__ import annotations
from typing import Dict, List


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        """
        LIFO Stack solution.
        Pushes opening brackets, pops and validates on closing brackets.
        """
        bracket_map: Dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack: List[str] = []

        for ch in s:
            if ch in bracket_map:
                # Closing bracket encountered
                top = stack.pop() if stack else "#"
                if top != bracket_map[ch]:
                    return False
            else:
                # Opening bracket encountered
                stack.append(ch)

        return len(stack) == 0


def run_tests() -> None:
    print("=== Testing LeetCode #20: Valid Parentheses ===")
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("{{{{}}}}", True),
        ("[{()}]", True),
        ("[(])", False),
    ]

    for s, expected in test_cases:
        res = Solution.isValid(s)
        assert res == expected, f"Failed on '{s}': expected {expected}, got {res}"

    print("[PASS] All LeetCode #20 test cases passed successfully!\n")


if __name__ == "__main__":
    run_tests()
