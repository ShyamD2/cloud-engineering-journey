"""
Day 5: Basic DSA — LeetCode #217: Contains Duplicate
Script: leetcode_217_contains_duplicate.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Time Complexity: O(N) using Hash Set / Hash Map
Space Complexity: O(N)
"""

from __future__ import annotations
from typing import List, Set


class Solution:
    @staticmethod
    def containsDuplicate_hashset(nums: List[int]) -> bool:
        """
        Idiomatic Python set length comparison.
        O(N) time to construct set, O(N) space.
        """
        return len(nums) != len(set(nums))

    @staticmethod
    def containsDuplicate_streaming(nums: List[int]) -> bool:
        """
        Early exit hash set tracking.
        Best Case: O(1) if duplicate is at the beginning.
        Average/Worst: O(N) time, O(N) space.
        """
        seen: Set[int] = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

    @staticmethod
    def containsDuplicate_sorting(nums: List[int]) -> bool:
        """
        In-place sorting approach without extra hash set allocation.
        Time: O(N log N)
        Space: O(1) extra space (in-place sort).
        """
        if len(nums) <= 1:
            return False
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False


def run_tests() -> None:
    print("=== Testing LeetCode #217: Contains Duplicate ===")
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([42], False),
        ([99, 99], True),
    ]

    for nums, expected in test_cases:
        res1 = Solution.containsDuplicate_hashset(nums)
        res2 = Solution.containsDuplicate_streaming(nums)
        res3 = Solution.containsDuplicate_sorting(nums)

        assert res1 == expected, f"Failed hashset on {nums}"
        assert res2 == expected, f"Failed streaming on {nums}"
        assert res3 == expected, f"Failed sorting on {nums}"

    print("[PASS] All LeetCode #217 test cases passed successfully across all implementations!\n")


if __name__ == "__main__":
    run_tests()
