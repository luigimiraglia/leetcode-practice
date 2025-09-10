# Problem: Unique Number of Occurrences
# Link: https://leetcode.com/problems/unique-number-of-occurrences/
# Difficulty: Easy
# Approach: Iterate through the array inserting values and their frequencies into a hash map
# Intert the frequencies in a new set and return false if there are duplicates
# Time complexity: O(n), space complexity O(n)

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurr = {}
        uniqueValues = set()

        for n in arr:
            if n not in occurr:
                occurr[n] = 1
            else:
                occurr[n] += 1

        for num, times in occurr.items():
            if times not in uniqueValues:
                uniqueValues.add(times)
            else:
                return False
        return True
