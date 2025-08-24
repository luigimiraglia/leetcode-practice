# Problem: Counting Bits
# Link: https://leetcode.com/problems/counting-bits/
# Difficulty: Easy
# Approach: Use DP with bit manipulation. For each number i,
#           the count of 1's is equal to arr[i >> 1] + (i & 1).

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)
        for i in range(n + 1):
            arr[i] = arr[i >> 1] + (i & 1)
        return arr
