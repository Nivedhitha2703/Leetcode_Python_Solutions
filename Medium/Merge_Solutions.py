from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        result = [intervals[0]]

        for start, end in intervals[1:]:

            last_start, last_end = result[-1]

            # Overlapping intervals
            if start <= last_end:
                result[-1][1] = max(last_end, end)

            # Non-overlapping interval
            else:
                result.append([start, end])

        return result
