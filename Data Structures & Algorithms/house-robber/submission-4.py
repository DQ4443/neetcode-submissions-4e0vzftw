class Solution:
    def rob(self, nums: List[int]) -> int:
        # for each position, can choose to take
        # nums[i] + nums[i - 2], nums[i-1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 1)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i - 1])

        print(dp)
        return max(dp[len(nums) - 1], dp[len(nums) - 2])