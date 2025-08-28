# Problem: Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i
# Difficulty: Easy
# Approach: Sliding Window
# Implement hash of size k
# Slide the window hash adding adding each time a new value and removing the last one
# Confront the sum with the greatest sum and repeat
# Return greatest sum / k

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        best = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            if window > best:
                best = window
        return best / k