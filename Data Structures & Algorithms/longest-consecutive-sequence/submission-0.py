class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            # check if start
            if num - 1 not in numset: 
                length = 1
                while num + length in numset:
                    length += 1
                if length > longest:
                    longest = length
        
        return longest


        # while next number in set, increment

