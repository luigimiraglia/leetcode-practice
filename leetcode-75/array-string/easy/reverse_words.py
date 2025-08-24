# Problem: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Easy
# Approach: Trim leading/trailing spaces, split on whitespace, reverse the list of words, then join with a single space.

def reverseWords(s: str) -> str:
    words = s.strip().split()
    return " ".join(reversed(words))
