# Problem: Find the Highest Altitude
# Link: https://leetcode.com/problems/find-the-highest-altitude/
# Difficulty: Easy
# Approach: Iterate through the array, adding each number to the counter
# and updating maxAlt if counter is greater than maxAlt
# Time complexity O(n), Space complexity O(1)

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        counter, maxAlt = 0, 0
        n = len(gain)
        for i in range(n):
            counter += gain[i]
            maxAlt = max(counter, maxAlt)
        return maxAlt
