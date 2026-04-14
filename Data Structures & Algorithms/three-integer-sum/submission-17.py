class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array, then for every number, do 2 pointer 2 sum
        res = set()
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r and 0 <= l < len(nums):
                currSum = num + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    res.add((num, nums[l], nums[r]))
                    l += 1

        res = [list(entry) for entry in res]

        return res
                    
