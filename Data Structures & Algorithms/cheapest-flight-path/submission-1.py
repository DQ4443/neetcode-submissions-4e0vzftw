class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # num_nodes limit, so use bellman ford. 

        prices = [float('inf')] * n
        prices[src] = 0

        # print(prices)

        for _ in range(k + 1):
            temp = prices.copy()

            for u, v, cost in flights:
                if prices[u] == float('inf'):
                    continue
                # print(prices)
                if prices[u] + cost < temp[v]:
                    temp[v] = prices[u] + cost

            prices = temp

        if prices[dst] == float('inf'):
            return -1
        return prices[dst]
                