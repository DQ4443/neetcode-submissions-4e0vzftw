class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graphs
        # dfs traverse graphs and increment counter
        # add node to visited each time

        counter = 0

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        for i in range(n):
            if i in visited:
                continue
            stack = [i]
            visited.add(i)
            while stack:
                curr = stack.pop()
                for neigh in graph[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)

            counter += 1

        return counter