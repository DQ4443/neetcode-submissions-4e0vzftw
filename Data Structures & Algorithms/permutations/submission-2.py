class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for each position: loop through all and add any unused ones
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return 
                
            if i > len(nums):
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])
            
        return res