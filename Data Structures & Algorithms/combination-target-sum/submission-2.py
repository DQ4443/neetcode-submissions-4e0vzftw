class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # exit cases: all nums done or target < 0 -> discard
        #             target == 0: append
        # each number you can either move on or add the number again

        res = []

        def backtrack(i, curr, left):
            if left == 0:
                res.append(curr[:])
                return
            
            if left < 0 or i >= len(nums):
                return 

            # include 
            backtrack(i, curr + [nums[i]], left - nums[i])

            # move on
            backtrack(i + 1, curr, left)

        backtrack(0, [], target)

        return res