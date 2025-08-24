# Problem: Greatest Common Divisor of Strings
# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Easy
# Approach: Check if str1 + str2 equals str2 + str1 (compatibility).
#           Use Euclidean algorithm to find gcd of lengths and return prefix.

def gcdOfStrings(str1: str, str2: str) -> str:
    # Helper function for gcd of two integers
    def gcd(a: int, b: int) -> int:
        return a if b == 0 else gcd(b, a % b)

    # If concatenations differ, no common divisor string exists
    if str1 + str2 != str2 + str1:
        return ""

    length = gcd(len(str1), len(str2))
    return str1[:length]
