# Problem: Asteroid Collision
# Link: https://leetcode.com/problems/asteroid-collision/
# Difficulty: Medium
# Approach: Create a stack for asteroids
# Iterate over given string and confront each new asteroid with the last in the stack before appending it to the stack
# Keep doing it while the asteroid is alive
# Time complexity O(n), Space complexity O(1)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for el in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and el < 0:
                if abs(stack[-1]) < abs(el):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(el):
                    stack.pop()
                alive = False
            if alive:
                stack.append(el)
        return stack
