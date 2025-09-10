# Problem: Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/
# Difficulty: Easy
# Approach: Create a prefix sum array
# Iterate over the new array checking if the sum of each index minus the
# number at that index is equal to the final sum minus the sum at that index
# Time complexity O(n), Space complexity O(1)

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sums, counter = [], 0
        for i in range(len(nums)):
            counter += nums[i]
            sums.append(counter)
        for i in range(len(nums)):
            if sums[i] - nums[i] == (counter - sums[i]):
                return i
        return -1
