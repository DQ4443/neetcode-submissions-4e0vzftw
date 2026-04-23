class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = num of ways to decode first i characters
        # dp[i] = dp[i - 1] if s[i] != 0 + dp[i - 2] if 10 <= s[i - 1:i + 1] <= 26

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
                print('hit')
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
                print('hit')

        return dp[n]