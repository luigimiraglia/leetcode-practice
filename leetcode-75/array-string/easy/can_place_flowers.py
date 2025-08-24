# Problem: Can Place Flowers
# Link: https://leetcode.com/problems/can-place-flowers/
# Difficulty: Easy
# Approach: Iterate through the array. If the current spot and its neighbors are empty (0),
#           place a flower and decrement n. Return True if able to place all flowers.

from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    left = n

    for i in range(len(flowerbed)):
        if (
            flowerbed[i] == 0 and
            (i == 0 or flowerbed[i - 1] == 0) and
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
        ):
            flowerbed[i] = 1
            left -= 1
            if left <= 0:
                return True

    return left <= 0
