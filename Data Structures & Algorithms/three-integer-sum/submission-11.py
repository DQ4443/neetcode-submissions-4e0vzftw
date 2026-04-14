class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ptr = 0
        res = []
        while ptr < len(nums):
            l, r = ptr + 1, len(nums) - 1
            num = nums[ptr]
            while l < r:

                if nums[l] + nums[r] + num == 0:
                    if [nums[ptr], nums[l], nums[r]] not in res:
                        res.append([nums[ptr], nums[l], nums[r]])
                    l += 1

                elif nums[l] + nums[r] > -num:
                    r -= 1

                else:
                    l += 1 

            ptr += 1


        return res
            