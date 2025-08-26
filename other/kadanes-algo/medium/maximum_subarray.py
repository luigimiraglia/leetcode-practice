# Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Approach: Kadane's Algorithm
# Iterate over the array once, keeping track of:
# - current sum (max subarray ending here)
# - maximum sum seen so far
# If current sum < 0, reset it to 0.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum, 0)
            curSum = curSum + num
            maxSum = max(curSum, maxSum)
        return maxSum