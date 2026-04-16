class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn's algo for topological sort + check cycle
            # get count of indegrees for each node
            # add all indegree 0 nodes to queue
            # pop and decrement neighbor indegrees
            # if 0, add to queue
            # keep track of num nodes processed.
            # if q is finished before all nodes visited: there is cycle

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)

        processed = 0
        while queue:
            curr = queue.popleft()
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
            processed += 1

        return processed == numCourses
