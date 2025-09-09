# Problem: Find the Difference of Two Arrays
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays
# Difficulty: Easy
# Approach: Insert values in two sets
# Calculate the difference using the - operator and convert the sets into strings before returning


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        A, B = set(nums1), set(nums2)

        return [list(A - B), list(B - A)]
