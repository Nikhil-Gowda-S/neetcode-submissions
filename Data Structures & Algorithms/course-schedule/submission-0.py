from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        res = []

        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1

        queue = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            res.append(cur)

            for adjnode in adj[cur]:
                indeg[adjnode] -= 1
                if indeg[adjnode] == 0:
                    queue.append(adjnode)

        return len(res) == numCourses