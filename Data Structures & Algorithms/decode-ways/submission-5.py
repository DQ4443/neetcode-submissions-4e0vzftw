class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[n] is num of ways to decode first n digits
        # add dp[i - 1] ways if last digit is not 0
        # add dp[i - 2] waysa if last two digits is valid -> [10, 26]

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 # 1 way to decode empty

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if i >= 2 and int(s[i - 2: i]) in range(10, 27):
                dp[i] += dp[i - 2]

        return dp[n]