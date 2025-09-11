# Problem: Increasing Triplet Subsequence
# Link: https://leetcode.com/problems/increasing-triplet-subsequence/
# Difficulty: Medium
# Approach: Initiate first and second as infinite
# Iterate through the array and replacing firt and second with current value to make them as low as possible
# Return true if number is greater than first and second
# Time complexity O(n), Space complexity O(1)

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
