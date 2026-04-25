class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can choose to buy, skip or sell. sell has 1 day cool down before buy again
        # state: i, holding
        # choice: if holding: try sell. if not holding: try buy
        # base: if i >= n: return 0
        # ans: dp(0, False)
        
        memo = {}
        n = len(prices)

        def dp(i, holding):
            if i >= n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            result = dp(i + 1, holding) # default to skip

            if holding: # try sell
                result = max(result, prices[i] + dp(i + 2, False))
            else: # try buy
                result = max(result, -prices[i] + dp(i + 1, True))

            memo[(i, holding)] = result
            return result

        return dp(0, False)