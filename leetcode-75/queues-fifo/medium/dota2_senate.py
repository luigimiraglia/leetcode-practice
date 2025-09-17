# Problem: Dota2 Senate
# Link: https://leetcode.com/problems/dota2-senate/
# Difficulty: Medium
# Approach: Queues
# Create two queues with the indexes of senators of both sides
# While both queues have senators pop the forst number of each queue
# Append the lowest number + the lenght of the senate back in the queue of the respective party
# Time complexity O(n), Space complexity O(n)s

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        senateLen = len(senate)

        for i, senator in enumerate(senate):
            if senator == 'D':
                dire.append(i)
            else:
                radiant.append(i)

        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()
            if d > r:
                radiant.append(r + senateLen)
            else:
                dire.append(d + senateLen)

        return 'Radiant' if radiant else "Dire"
