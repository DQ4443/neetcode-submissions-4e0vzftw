class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find

        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return [u, v]
            parent[pu] = pv