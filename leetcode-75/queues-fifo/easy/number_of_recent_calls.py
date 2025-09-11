# Problem: Number of Recent Calls
# Link: https://leetcode.com/problems/number-of-recent-calls/
# Difficulty: Easy
# Approach: Create a queue for the requests
# Log each request into the queue and remove any request that is older than 3000ms
# Return queue lenght
# Time complexity O(n), Space complexity O(1)

from collections import deque


class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:

        self.counter.append(t)
        while (self.counter[0] < (t - 3000)):
            self.counter.popleft()

        return len(self.counter)
