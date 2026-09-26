"""
Day 4: Basic DSA — LeetCode #1929: Concatenation of Array
Script: leetcode_1929_concatenation.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Problem Statement:
Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from __future__ import annotations
from typing import List


class Solution:
    @staticmethod
    def getConcatenation_operator(nums: List[int]) -> List[int]:
        """Idiomatic Python list multiplication/concatenation."""
        return nums + nums

    @staticmethod
    def getConcatenation_extend(nums: List[int]) -> List[int]:
        """Using in-place copy and extend."""
        ans = list(nums)
        ans.extend(nums)
        return ans

    @staticmethod
    def getConcatenation_preallocated(nums: List[int]) -> List[int]:
        """Pre-allocated array assignment (C/Go systems-style)."""
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans


def run_tests() -> None:
    print("=== Testing LeetCode #1929: Concatenation of Array ===")
    test_cases = [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([0], [0, 0]),
        ([], []),
        ([5, -2, 10], [5, -2, 10, 5, -2, 10]),
    ]

    for nums, expected in test_cases:
        res1 = Solution.getConcatenation_operator(nums)
        res2 = Solution.getConcatenation_extend(nums)
        res3 = Solution.getConcatenation_preallocated(nums)

        assert res1 == expected, f"Failed operator for {nums}: got {res1}, expected {expected}"
        assert res2 == expected, f"Failed extend for {nums}: got {res2}, expected {expected}"
        assert res3 == expected, f"Failed preallocated for {nums}: got {res3}, expected {expected}"

    print("[PASS] All LeetCode #1929 test cases passed successfully across all implementations!\n")


if __name__ == "__main__":
    run_tests()
