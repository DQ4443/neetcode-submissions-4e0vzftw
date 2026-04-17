class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # can either include or not include each item
        # append when subarray has gone through all num in nums

        res = []

        def backtrack(i, current):
            if i == len(nums):
                res.append(current[:])
                return 

            # include nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

            # exclude nums[i]
            backtrack(i + 1, current)

        backtrack(0, [])

        return res