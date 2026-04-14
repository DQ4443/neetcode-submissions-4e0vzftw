class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance from origin = sqrt(x^2 + y^2)
        # can just compare x^2 + y^2
        # nlog(k) runtime, so use heap to keep track of top k

        heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (distance, x, y))

        res = []
        count = 0
        while count < k:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
            count += 1

        return res 

