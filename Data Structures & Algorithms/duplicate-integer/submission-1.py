class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set
        return len(nums) != len(set(nums))