class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # compare two strings, keep track of two pointers; if match move on, otherwise 1 + min(three ops)
        # state: i, j
        # choice: if match: dp(i + 1, j + 1); else 1 + min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1))
        # base: if i or j runs out, add the rest as add operations
        # ans: dp(0, 0)

        memo = {}
        m, n = len(word1), len(word2)

        def dp(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                result = dp(i + 1, j + 1)
            else:
                result = 1 + min(
                    dp(i, j + 1),
                    dp(i + 1, j),
                    dp(i + 1, j + 1)
                )

            memo[(i, j)] = result
            return result

        return dp(0, 0)