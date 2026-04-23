class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[n] = fewest coins needed to make up n
        # each step has choice to take 1 + min(coins)

        memo = {}

        def recurse(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            if remaining in memo:
                return memo[remaining]

            result = float('inf')
            for coin in coins:
                result = min(result, 1 + recurse(remaining - coin))

            memo[remaining] = result
            return result

        res = recurse(amount)
        
        return res if res != float('inf') else -1
