# Problem: Max Number of K-Sum Pairs
# Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Difficulty: Medium
# Approach: Two sum
# Created a counter object and count the occurrences of each value
# iterated through the array and check if the number that summed to the current value occurs in the array
# If true remove an occurrence of both the surrent and the target value from the counter and add 1 to operations
# If the current number is half the target and only appears once skip that iteration
# Return total operations
# Time complexity O(n), Space complexity O(n)

from collections import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        c = Counter(nums)
        operations = 0

        for n in nums:
            if k - n == n and c[n] == 1:
                continue
            if c[k - n] > 0 and c[n] > 0:

                c[k - n] -= 1
                operations += 1
                c[n] -= 1

        return operations
