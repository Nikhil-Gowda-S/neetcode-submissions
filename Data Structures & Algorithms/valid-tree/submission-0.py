class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        def dfs(node,prev):
            if node in vis:
                return False
            vis.add(node)
            for adjnode in adj[node]:
                if adjnode==prev:
                    continue
                ans=dfs(adjnode,node)
                if ans==False:
                    return False
            return True
        return dfs(0,-1) and n==len(vis)
        