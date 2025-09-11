# Problem: Removing Stars From a String
# Link: https://leetcode.com/problems/removing-stars-from-a-string/
# Difficulty: Medium
# Approach: Create a stack and iterate over string chars
# If char is a star execute pop on stack
# Else append c to the stack
# Join and return stack as a string
# Time complexity O(n), Space complexity O(1)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
