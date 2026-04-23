class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp bottom up
        # state: cmin and cmax
        # choice: nums[i], nums[i] * cmax, nums[i] * cmin
        # base: cmax = nums[i], cmin = nums[i]
        # ans: anywhere, so max of everything. keep track with res var

        n = len(nums)
        res = nums[0]
        cmax = nums[0]
        cmin = nums[0]

        for i in range(1, n):
            choices = (nums[i], nums[i] * cmax, nums[i] * cmin)
            cmax = max(choices)
            cmin = min(choices)
            res = max(res, cmax)

        return res