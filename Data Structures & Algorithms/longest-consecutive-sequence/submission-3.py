class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to basically check for if neighboring consecutive elements exist -> use set
        # only consider the start of each sequence (no left neighbors)
        # if a num has no left neighbor, while the right neighbor exists, increment
        # store max length and return it
        if not nums:
            return 0

        numSet = set(nums)
        longest = 0

        for num in nums:
            # start of sequence
            if num - 1 not in numSet:
                length = 1
                while num + 1 in numSet:
                    length += 1
                    num += 1
                longest = max(longest, length)
        
        return longest
