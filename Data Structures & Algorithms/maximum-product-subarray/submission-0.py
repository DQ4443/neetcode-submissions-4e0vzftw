class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # state: need to keep track of largest positive and smallest negative
        # candidates: (nums[i], curr_max * nums[i], curr_min * nums[i])
        # base case: nums[1] is it's own max and min
        # answer: can be anywhere, so return max of whole thing
        # order: left to right (bottom up)
        n = len(nums)
        result = nums[0]
        cmax = nums[0]
        cmin = nums[0]

        for i in range(1, n):
            candidates = (nums[i], cmax * nums[i], cmin * nums[i])
            cmax = max(candidates)
            cmin = min(candidates)
            result = max(result, cmax)

        return result