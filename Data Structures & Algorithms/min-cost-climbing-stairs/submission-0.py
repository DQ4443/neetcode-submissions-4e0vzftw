class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at every step, cost = cost[i] + min(cost[i - 1], cost[i - 2])
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i- 1], dp[i-2])

        return min(dp[n - 1], dp[n - 2])

