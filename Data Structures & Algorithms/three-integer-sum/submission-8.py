class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        print("hello")
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            num = nums[i]
            while l < r:

                if nums[l] + nums[r] + num == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1

                elif nums[l] + nums[r] > -num:
                    r -= 1

                else:
                    l += 1 


        return res
            