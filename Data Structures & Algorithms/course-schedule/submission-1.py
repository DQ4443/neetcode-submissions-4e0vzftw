class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn's algorithm
        # get indegrees of each graph node
        # keep track of node neighbors with map
        # add all indegree 0 nodes to queue
        # pop node, and decrement all it's neighbors
        # if 0, add to queue
        # keep track of total nodes and how many visited
        # if visisted ≠ total, there is a cycle

        graph = defaultdict(list)
        inorder = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            inorder[crs] += 1

        queue = deque(i for i in range(numCourses) if inorder[i] == 0)

        visited = 0
        while queue:
            visited += 1
            curr = queue.popleft()
            for neigh in graph[curr]:
                inorder[neigh] -= 1
                if inorder[neigh] == 0:
                    queue.append(neigh)

        return visited == numCourses