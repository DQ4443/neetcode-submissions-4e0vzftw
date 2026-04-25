class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp bottom up (list building)
        # define dp[i] as LIS ending at index i
        # state: i
        # choice: check every number before i, if dp[j] < dp[i], then choose the largest and set to 1 + dp[j]
        # base: every index should start off as 1 (itself)
        # ans: can be anywhere, so return max of list
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)