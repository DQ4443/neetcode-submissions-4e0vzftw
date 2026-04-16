class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # kahn's algorithm
        # keep track of order of popping

        order = []
        graph = defaultdict(list)
        inorder = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            inorder[crs] += 1

        queue = deque(i for i in range(numCourses) if inorder[i] == 0)

        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neigh in graph[curr]:
                inorder[neigh] -= 1
                if inorder[neigh] == 0:
                    queue.append(neigh)

        if len(order) != numCourses:
            return []
        return order