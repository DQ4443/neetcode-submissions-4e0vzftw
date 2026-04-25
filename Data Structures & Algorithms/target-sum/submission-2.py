class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for each number, can choose to add or subtract
        # state: i, total
        # choice: dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])
        # base/exit: total == target: +1, i >= n or total > target: 0
        # ans: dp(0, 0)

        memo = {}
        n = len(nums)

        def dp(i, total):
            if total == target and i == n:
                return 1
            if i >= n:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            result = dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])
            
            memo[(i, total)] = result
            return result

        return dp(0, 0)