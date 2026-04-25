class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # key idea: choose to use 1 coin again or move onto the next (never using previous again)
        # state: i, remaining
        # choice: dp(i, remaining - coins[i]) + dp(i + 1, remaining)
        # base/exit: remaining == 0 : +1, i >= n: 0
        # ans: dp(0, amount)

        memo = {}
        n = len(coins)

        def dp(i, remaining):
            if remaining == 0:
                return 1
            if i >= n or remaining < 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            result = dp(i, remaining - coins[i]) + dp(i + 1, remaining)

            memo[(i, remaining)] = result
            return result

        return dp(0, amount)