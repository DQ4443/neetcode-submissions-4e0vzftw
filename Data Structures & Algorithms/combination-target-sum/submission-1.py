class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # exit cases: all nums done or target < 0 -> discard
        #             target == 0: append
        # each number you can either move on or add the number again
        
        res = []

        def backtrack(i, curr, remaining):
            # append case
            if remaining == 0:
                # print(f'valid: {curr}')
                res.append(curr[:])
                # print(res)
                return

            if remaining < 0 or i >= len(nums):
                return

            # include case:
            curr.append(nums[i])
            # print(f'inlclude: {curr}')
            backtrack(i, curr, remaining - nums[i])
            curr.pop()

            # move on case:
            # print(f'move on: {curr}')
            backtrack(i + 1, curr, remaining)

        backtrack(0, [], target)

        # print(res)
        return res