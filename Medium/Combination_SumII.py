class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        result = []

        def backtrack(start, remaining, path):

            # Target reached
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                # Choose
                path.append(candidates[i])

                # Each element can be used only once
                backtrack(i + 1, remaining - candidates[i], path)

                # Undo
                path.pop()

        backtrack(0, target, [])

        return result
