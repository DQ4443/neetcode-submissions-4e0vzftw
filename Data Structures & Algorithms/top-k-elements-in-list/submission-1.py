class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort O(n)
        freqs = [[] for _ in range(len(nums) + 1)] # max if all letters same
        print(freqs)

        # count the frequency of each number and store in dict
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        print(counts)
        
        for key, value in counts.items():
            freqs[value] += [key]
        
        # get top k
        res = []
        for i in range(len(nums), 0, -1):
            res += freqs[i]

            if len(res) == k:
                return res

        return []