class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets, freq)

        for entry in freq:
            buckets[freq[entry]].append(entry)

        print(buckets)

        res = []
        for entry in buckets:
            res += entry
        print(res)
        return res[-k:]
