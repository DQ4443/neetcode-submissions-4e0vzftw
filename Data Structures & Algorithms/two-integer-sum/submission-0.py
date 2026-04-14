class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hash map
        comp = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in comp:
                return [comp[num], i]
            else:
                comp[target - num] = i

        return -1