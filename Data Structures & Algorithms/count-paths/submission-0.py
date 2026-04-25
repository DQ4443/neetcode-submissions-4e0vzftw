class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2d dp: top down
        # at any point, can move down or right

        # state: a, b
        # choice: dp(a + 1, b) + dp(a, b + 1)
        # base: increment res if a == m - 1 and b == n - 1
        # ans: dp[0][0]

        memo = {}
        
        def dp(a, b):
            if a == m - 1 and b == n - 1:
                return 1

            if a >= m or b >= n:
                return 0

            if (a, b) in memo:
                return memo[(a, b)]

            res = dp(a + 1, b) + dp(a, b + 1)

            print(res)

            memo[(a, b)] = res
            return res

        return dp(0, 0)
