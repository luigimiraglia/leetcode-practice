# Problem: Max Consecutive Ones III
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
# Difficulty: Medium
# Approach: Two pointers
# Right pointer advances counting zeros
# If zeros in window are more than the available swaps, left pointer adjusteds de window until a zero is removed
# Keep track of max window length and return it
# Time complexity O(n), Space complexity O(1)

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        L, best, zeros = 0, 0, 0

        for R in range(len(nums)):
            if nums[R] == 0:
                zeros += 1
                while zeros > k and L <= R:
                    if nums[L] == 0:
                        zeros -= 1
                    L += 1

            best = max(best, R - L + 1)
        return best
