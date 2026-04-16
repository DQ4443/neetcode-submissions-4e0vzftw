class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree means n - 1 edges
        # build graph from edges
        # dfs traverse graph
        # keep track of visited nodes
        # if all nodes visited: valid

        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = {0}
        stack = [0]
        while stack:
            curr = stack.pop()
            for neigh in graph[curr]:
                if neigh not in visited:
                    stack.append(neigh)
                    visited.add(neigh)

        return len(visited) == n