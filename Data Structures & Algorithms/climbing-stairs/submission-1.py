class Solution:
    def climbStairs(self, n: int) -> int:
        # at every step[i], ways to get there = ste[i - 1] + step[i - 2]
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]