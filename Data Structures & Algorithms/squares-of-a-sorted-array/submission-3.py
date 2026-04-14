class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # easier to start at both ends and just increment toward middle

        if not nums:
            return []

        l, r = 0, len(nums) - 1
        res = []

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res = [nums[r] ** 2] + res
                r -= 1
            else:
                res = [nums[l] ** 2] + res
                l += 1

        return res

