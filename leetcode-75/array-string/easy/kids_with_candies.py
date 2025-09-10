# Problem: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy
# Approach: Find the current maximum and check for each kid if adding extraCandies reaches/exceeds it.

from typing import List


def kidsWithCandies(candies: list[int], extraCandies: int) -> List[bool]:
    most_candies = max(candies)
    return [kid + extraCandies >= most_candies for kid in candies]
