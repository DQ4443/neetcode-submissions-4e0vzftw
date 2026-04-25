class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # iterate pointer through both strings
        
        # state: i, j
        # choice: if letter match, take. else, increment or other
        # base: if i >= len(text1) or j >= len(text2), end
        # ans: dp(0, 0)

        memo = {}
        m = len(text1)
        n = len(text2)

        def dp(a, b):
            if a >= m or b >= n:
                return 0

            if (a, b) in memo:
                return memo[(a, b)]

            if text1[a] == text2[b]:
                result = 1 + dp(a + 1, b + 1)
            else:
                result = max(dp(a + 1, b), dp(a, b + 1))

            memo[(a, b)] = result

            return result

        return dp(0, 0)