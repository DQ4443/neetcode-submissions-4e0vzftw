class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # use bellman ford since k stops constraints
        # make prices array and set inital all to inf, starting to 0
        # k stops, so total k + 2 nodes or k + 1 edges. repeat k + 1 times

        # make copy of prices each run to reference pre update values
        # iterate through edges and skip unvisited starting nodes

        prices = [float('inf')] * n
        prices[src] = 0
        print(prices)

        for _ in range(k + 1):
            temp = prices.copy()
            for u, v, cost in flights:
                print(u, v, cost)
                if prices[u] == float('inf'):
                    continue 
                if prices[u] + cost < temp[v]:
                    print('hit')
                    temp[v] = prices[u] + cost

            prices = temp
            print(prices)

        return -1 if prices[dst] == float('inf') else prices[dst]