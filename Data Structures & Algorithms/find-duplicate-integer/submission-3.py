class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use linked list cycle detection
        # nums[curr] for curr.next
        # use cycle start finding algo after

        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        print(slow, fast)

        slow = nums[0]

        while True:
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[fast]
