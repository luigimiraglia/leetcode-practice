# Problem: Determine if Two Strings Are Close
# Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium
# Approach: Hash Maps/Sets
# Return false if the lengths are different
# Use the counter method to create a dict for each word
# Return true if the letters and the frequencies are the same for each word
# Time complexity O(nlogn), Space complexity O(n)

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counts1, counts2 = Counter(word1), Counter(word2)

        return (counts1.keys() == counts2.keys()) and (sorted(counts1.values()) == sorted(counts2.values()))
