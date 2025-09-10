# Problem: Nearest Exit from Entrance in Maze
# Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Difficulty: Medium
# Approach: BFS. Start from the entrance and explore neighbors (up, down, left, right).
#           Stop when the first boundary cell (different from entrance) is reached.

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        sr, sc = entrance
        q = deque([(sr, sc, 0)])
        visited = {(sr, sc)}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, d = q.popleft()
            # If on border (but not the entrance), it's an exit
            if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and (r, c) != (sr, sc):
                return d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1
