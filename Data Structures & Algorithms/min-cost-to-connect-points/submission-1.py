class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims. add closest node outside of tree
        # repeat until no unvisited nodes left
        # use minheap pq { (distance, node)}

        N = len(points)
        visited = set()
        heap = [(0, 0)] # distance 0 for 0th node
        total = 0

        while len(visited) < N:
            # print(heap)
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total += cost
            # print(N)
            for j in range(N):
                # print(j)
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))

        return total


        