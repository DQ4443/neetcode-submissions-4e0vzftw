class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use heap, size k
        # remove lowest, so min heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        return heap[0]