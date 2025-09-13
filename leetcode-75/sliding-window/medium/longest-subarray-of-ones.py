# Problem: Longest Subarray of 1's After Deleting One Element
# Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Difficulty: Medium
# Approach: Sliding Window
# Initialized left and right pointers
# Move R through the array and move left to make the window contain onem zero at max
# Return the number of ones in the window and subtract one if there are no zeros
# Time complexity O(n), Space complexity O(1)

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        L, maxLength, zeros = 0, 0, 0

        for R, x in enumerate(nums):
            if x == 0:
                zeros += 1
                while zeros > 1:
                    if nums[L] == 0:
                        zeros -= 1
                    L += 1
            maxLength = max(maxLength, R - L - zeros + 1)

        if zeros == 0:
            return maxLength - 1
        return maxLength
