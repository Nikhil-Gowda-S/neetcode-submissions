from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        indeg=[0]*numCourses
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u]+=1
        queue=deque()
        for i in range(numCourses):
            if indeg[i]==0:
                queue.append(i)
        while len(queue)!=0:
            cur=queue.popleft()
            res.append(cur)
            for adjnode in adj[cur]:
                indeg[adjnode]-=1
                if indeg[adjnode]==0:
                    queue.append(adjnode)
        if len(res)==numCourses:
            return res
        return []


        