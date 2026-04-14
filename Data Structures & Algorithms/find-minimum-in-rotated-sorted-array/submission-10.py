class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        low, high = 0, len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] >= nums[low]:
                res = min(res, nums[mid], nums[low], nums[high])
                low = mid + 1
            else:
                res = min(res, nums[mid], nums[low], nums[high])
                high = mid - 1

        return res