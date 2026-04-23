class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down intuition:
        # dp(n) = num ways to make up n amount
        # dp(i) = 1 + min(dp(i - coin)) for each coin

        memo = {}

        def dp(i):
            if i == 0:
                return 0
            
            if i < 0:
                return float('inf')

            if i in memo:
                return memo[i]

            step = float('inf')
            for coin in coins:
                step = min(step, 1 + dp(i - coin))

            memo[i] = step
            return step

        res = dp(amount)

        if res == float('inf'):
            return -1

        return res