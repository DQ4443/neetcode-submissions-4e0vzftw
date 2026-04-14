class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for entry in freq:
            buckets[freq[entry]].append(entry)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) >= k:
                return res[:k]