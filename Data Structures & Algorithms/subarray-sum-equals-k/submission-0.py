class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # keep prefix sums in a hashmap
        # idea is at every new element, if there is some prefix such that
        # sum[0..new] - sum(some sub array) == k, then count += 1
        # so every new element, add the current prefix into the prefixsum hashmap

        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        prefix = count = 0
        for num in nums:
            prefix += num
            if prefix - k in prefixSums:
                count += prefixSums[prefix - k]
            prefixSums[prefix] += 1
        
        return count
