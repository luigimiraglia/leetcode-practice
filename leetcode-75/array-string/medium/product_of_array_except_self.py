# Problem: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Approach: Prefix sum
# Create array and insert products of values left to the current value
# Calculate product of values right to the current value and multiply them in place with the products of the left values
# Time complexity O(n), Space complexity O(1)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products, left, right = [], 1, 1
        l = len(nums)
        for i in range(l):
            products.append(left)
            left = left * nums[i]
        for i in range(l):
            products[l - 1 - i] = products[l - 1 - i] * right
            right = right * nums[l - 1 - i]

        return products
