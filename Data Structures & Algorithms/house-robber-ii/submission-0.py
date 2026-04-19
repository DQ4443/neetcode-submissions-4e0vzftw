class Solution:
    def rob(self, nums: List[int]) -> int:
        # only difference from house robbers 1 is that 0 and -1 are neigh
        # can choose either [1:] or [:-1] to rob
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob(houses):
            k = len(houses)

            if k == 1:
                return houses[0]

            dp = [0] * k

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, k):
                dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])

            return dp[k - 1]

        return max(rob(nums[:-1]), rob(nums[1:]))