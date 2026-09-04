class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            # If already calculated, return stored result
            if start in memo:
                return memo[start]

            # Reached the end of the string
            if start == len(s):
                return [""]

            result = []

            # Try every possible word starting from 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    # Find all possible sentences for remaining string
                    remaining_sentences = dfs(end)

                    for sentence in remaining_sentences:
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return dfs(0)
