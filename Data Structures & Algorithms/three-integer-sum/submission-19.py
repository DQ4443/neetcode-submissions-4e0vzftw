class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array, then for every number, do 2 pointer 2 sum
        # to prevent dups: skip duplicate i, and after finding a match, skip dup l and dup r
        res = []
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
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # avoid left dups
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # avoid right dups
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
                    
