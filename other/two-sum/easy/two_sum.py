# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Approach: Two sum
# Create a hashmap
# Iterate through the array checking for every number the other number
# needed to reach the target is in the hashmap
# Add current number and index to the hashmap
# Time complexity O(n), Space complexity O(1)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [i, seen[target - x]]
            seen[x] = i
