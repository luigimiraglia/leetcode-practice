# Problem: Leaf-Similar Trees
# Link: https://leetcode.com/problems/leaf-similar-trees/
# Difficulty: Easy
# Approach: Perform DFS on both trees, collect leaf values in order, then compare the two lists.

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaves(node: Optional[TreeNode], leaves: list[int]) -> None:
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            findLeaves(node.left, leaves)
            findLeaves(node.right, leaves)

        leaves1, leaves2 = [], []
        findLeaves(root1, leaves1)
        findLeaves(root2, leaves2)
        return leaves1 == leaves2
