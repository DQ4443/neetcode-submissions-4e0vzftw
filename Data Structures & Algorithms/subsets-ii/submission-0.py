class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort first to skip duplicates
        nums.sort()
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return 

            if i > len(nums):
                return

            # include case
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, curr)

        backtrack(0, [])

        return res