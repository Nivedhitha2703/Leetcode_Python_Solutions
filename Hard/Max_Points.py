from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        answer = 1

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Reduce the slope using GCD
                g = gcd(dx, dy)

                dx //= g
                dy //= g

                # Normalize the sign
                if dx < 0:
                    dx *= -1
                    dy *= -1

                # Handle vertical lines
                if dx == 0:
                    dy = 1

                # Handle horizontal lines
                if dy == 0:
                    dx = 1

                slopes[(dy, dx)] += 1

                answer = max(answer, slopes[(dy, dx)] + 1)

        return answer
