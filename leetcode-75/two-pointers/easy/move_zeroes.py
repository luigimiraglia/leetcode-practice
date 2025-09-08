# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Approach: Two pointers, Left and Right pointers start from first and second position
# While Right pointer's cell value is not 0 Right pointer increases
# If Left pointer's cell value is 0 swaps value with Right pointer's
# Iterates through the entire array
# Time complexity O(n), Space complexity O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        L, R = 0, 1
        n = len(nums)
        while R < n:
            while R < n and nums[R] == 0:
                R += 1
            if R == n:
                break
            if nums[L] == 0:
                temp = nums[R]
                nums[R] = nums[L]
                nums[L] = temp
                L += 1
                R += 1
            else:
                L += 1
            if L == R:
                R += 1
