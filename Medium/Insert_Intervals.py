from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        start, end = newInterval

        for s, e in intervals:

            # Case 1: Current interval is completely before newInterval
            if e < start:
                result.append([s, e])

            # Case 2: Current interval is completely after newInterval
            elif s > end:
                result.append([start, end])
                start, end = s, e

            # Case 3: Overlapping intervals
            else:
                start = min(start, s)
                end = max(end, e)

        # Add the remaining newInterval
        result.append([start, end])

        return result
