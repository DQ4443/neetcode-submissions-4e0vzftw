class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstras. use minheap pq, and dist map 
        # build graph first with weights 
        graph = defaultdict(list)

        for start, end, weight in times:
            graph[start].append((end, weight))

        print(f'graph: {graph}')

        dist = {}
        pq = [(0, k)] # pq sorted by distance, so (d, node)

        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d

            for neigh, weight in graph[node]:
                heapq.heappush(pq, (d + weight, neigh))

        print(f'dist: {dist}')

        if len(dist) == n:
            return max(dist.values())
            
        return -1
