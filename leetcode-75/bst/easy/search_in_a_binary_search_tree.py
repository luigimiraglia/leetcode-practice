# Problem: Search in a Binary Search Tree
# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Difficulty: Easy
# Approach: Recursively traverse the BST. If current node matches the value, return it;
#           if value is smaller, search the left subtree; otherwise, search the right.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
