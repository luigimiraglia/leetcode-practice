# Problem: Is Subsequence
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
# Approach: Two pointers, while one iterates through the s string the other iterates through t
# to find matching values. Pointer R moves left until finds all the s chars in string t
# If string t is empty and s isn't, function returns false
# Time complexity O(n), Space complexity O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        R = 0
        n = len(t)
        if n == 0 and len(s) != 0:
            return False

        for c in s:
            while R < n and t[R] != c:
                R += 1
            if R >= n:
                return False
            R += 1
        return True
