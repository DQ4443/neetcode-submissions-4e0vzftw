class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp bottom up
        # define dp[n] as LIS ending at nth letter
        # state: i
        # choice: dp[i] = 1 or if there is a previous number smaller, 1 + dp[j] for j in range(i)
        # base: i = 0, every element starts as 1
        # ans: could be anywhere, return max

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])


        return max(dp)