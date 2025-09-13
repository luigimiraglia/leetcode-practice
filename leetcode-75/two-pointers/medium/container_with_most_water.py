# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Approach: Two pointers
# L and R pointers initialized at the start and end of the array
# Calculate the current volume then make pointer that points to the minimum value
# move towards the other in the array
# Repeat keeping track of max volume while L < R
# Time complexity O(n), Space complexity O(1)


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = len(height)
        R = l - 1
        maxVolume, curVolume = 0, 0
        for L in range(l):
            if L < R:
                curVolume = (R - L) * min(height[R], height[L])
                maxVolume = max(maxVolume, curVolume)
                while height[L] > height[R]:
                    R -= 1
                    curVolume = (R - L) * min(height[R], height[L])
                    maxVolume = max(maxVolume, curVolume)
        return maxVolume
