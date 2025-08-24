# Problem: Keys and Rooms
# Link: https://leetcode.com/problems/keys-and-rooms/
# Difficulty: Medium
# Approach: BFS using a queue (deque). Start from room 0, visit all reachable rooms by following keys.
#           Keep a visited set and return True if all rooms are visited.

from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        q = deque([0])

        while q:
            room = q.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)

        return len(visited) == len(rooms)
