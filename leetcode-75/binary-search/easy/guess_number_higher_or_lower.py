# Problem: Guess Number Higher or Lower
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/
# Difficulty: Easy
# Approach: Binary search. Narrow down the range based on the guess API result until the correct number is found.

# The guess API is already defined for you:
# def guess(num: int) -> int:
#    -1 if num is higher than the picked number
#     1 if num is lower than the picked number
#     0 if num is equal to the picked number

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result < 0:
                right = mid - 1
            else:
                left = mid + 1
