class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algorithm. repeated add closest none tree node
        # use minheap pq to store closest
        # repeat until all nodes added
        # mark on pop, keep track of total weight

        N = len(points)
        visited = set()
        heap = [(0, 0)] # (cost, node_idx)
        total = 0

        while heap:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)

            total += cost
            for j in range(N):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))

        return total