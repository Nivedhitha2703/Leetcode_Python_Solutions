class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        # dp[i] means s[0:i] can be segmented
        dp = [False] * (n + 1)

        # Empty string is always valid
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                # Check if:
                # 1. First part can be segmented
                # 2. Current substring is a dictionary word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
