class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(nums[low], nums[high])

            if nums[mid] == target:
                return mid
            
            # find which half of the sorted you are in
            if nums[low] <= nums[mid]: # right side
                if nums[mid] < target or nums[low] > target:
                    low = mid + 1
                else:
                    high = mid - 1
            else: # left side
                if nums[mid] > target or nums[high] < target:
                    high = mid - 1
                else:
                    low = mid + 1
            
        return -1
