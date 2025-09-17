# Problem: Decode String
# Link: https://leetcode.com/problems/decode-string/
# Difficulty: Medium
# Approach: Stacks
# Create a stack and add the characters from the strings until you encounter a ]
# When encountered a ], pop the chars into a temp string until you find [
# Once [ is found, delete [ and start constructing the number in a new string by adding the
# Digits as you pop them from the sack while you keep encountering digits
# Take result string mutiplied by the number and add it to the stack
# Repeat
# Return the joint strings inside the stack
# Time complexity O(n), Space complexity O(m)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr = ""
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(curr * int(num))
        return "".join(stack)
