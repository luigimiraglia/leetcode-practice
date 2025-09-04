# Problem: Maximum Number of Vowels in a Substring of Given Length
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# Difficulty: Medium
# Approach: Sliding window of variable lenght with left and right pointer
# The right pointer moves left counting vowels into the vindow until vindow reaches lenght k
# Max value is updater when window size reaches k
# Then left pointer moves a spot right checking if it was on a vowel and updates the count
# Reiterate
# Time complexity O(n), space complexity O(1)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, total, maxValue = 0, 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for R in range(len(s)):
            if s[R] in vowels:
                total += 1
            maxValue = max(maxValue, total)
            if (R - l + 1) >= k:
                if s[l] in vowels:
                    total -= 1
                l += 1

        return maxValue
