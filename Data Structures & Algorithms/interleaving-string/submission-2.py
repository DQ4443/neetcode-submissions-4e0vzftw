class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # choose to put s1[i] or s2[j]
        # state: i, j
        # choice: dp(i + 1, j) or dp(i, j + 1); check if i < m and s3[i + j + 1] == s[i + 1] etc
        # base: if i == m and j == n: True
        # ans: dp(0, 0)
        memo = {}  
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False

        def dp(i, j):
            if i == m and j == n:
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            result = False
            if i < m and s3[i + j] == s1[i]:
                result = result or dp(i + 1, j)
            if j < n and s3[i + j] == s2[j]:
                result = result or dp(i, j + 1)

            memo[(i, j)] = result
            return result
        
        return dp(0, 0)