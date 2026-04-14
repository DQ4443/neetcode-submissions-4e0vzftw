class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use linked list, follow the number to the position in the array
        # algorithm to find the start of the cycle

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # cycle finding: put pointer at start, then move both pointers
        # 1 step at a time until meet. 

        slow = 0

        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow