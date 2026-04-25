class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # top down dp
        # try to hit sum(nums) // 2
        # can choose to include or skip for every num

        # state: i, remaining
        # choice: dp(i + 1, remaining - nums[i]) or dp(i + 1, remaining)
        # base: target == 0 means found, target < 0 or i > 1 means no exist
        # ans: dp(0, sum(nums) // 2)

        memo = {}
        n = len(nums)

        total = sum(nums)
        if total % 2 == 1:
            print('hit base')
            return False

        def dp(i, remaining):
            if remaining == 0:
                return True

            if remaining < 0 or i >= n:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            result = dp(i + 1, remaining - nums[i]) or dp(i + 1, remaining)

            memo[(i, remaining)] = result

            return result

        return dp(0, total // 2)