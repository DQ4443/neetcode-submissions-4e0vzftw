class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's
        # use minheap pq [(distance, node)]
        # build distance map {node: distance}

        # build graph
        graph = defaultdict(list) # {node: (neigh, weight)}
        for u, v, w in times:
            graph[u].append((v, w))
        # print(graph)
        
        pq = [(0, k)]
        dist = {}

        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            # print(f'node: {node}')
            # print(node, graph[node])
            for neigh, weight in graph[node]:
                heapq.heappush(pq, (d + weight, neigh))

        # print(dist)

        return max(dist.values()) if len(dist) == n else -1