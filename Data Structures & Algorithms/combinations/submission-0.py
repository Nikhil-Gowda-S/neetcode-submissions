class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def solve(i,sub):
            sub.append(i)
            if len(sub)==k:
                res.append(sub[:])
                sub.pop()
                return
            
            for x in range(i+1,n+1):
                solve(x,sub)
            sub.pop()

        for i in range(1,n+1):
            solve(i,[])

        return res
        