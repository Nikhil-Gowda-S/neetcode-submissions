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


"""class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, sub):
            if len(sub) == k:
                res.append(sub[:])
                return

            for i in range(start, n + 1):
                sub.append(i)
                backtrack(i + 1, sub)
                sub.pop()

        backtrack(1, [])
        return res """
        