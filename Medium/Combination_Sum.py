class Solution:
    def combinationSum(self, candidates, target):

        result = []

        candidates.sort()

        def backtrack(start, remaining, path):

            # Target reached
            if remaining == 0:
                result.append(path.copy())
                return

            # Try candidates
            for i in range(start, len(candidates)):

                num = candidates[i]

                # Since candidates is sorted,
                # no later number can work either
                if num > remaining:
                    break

                # Choose
                path.append(num)

                # Reuse the same number
                backtrack(i, remaining - num, path)

                # Undo
                path.pop()

        backtrack(0, target, [])

        return result
