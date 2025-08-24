# Problem: Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Approach: Iterate through both strings up to the max length and alternate characters.

def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    max_length = max(len(word1), len(word2))

    for i in range(max_length):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return "".join(result)
