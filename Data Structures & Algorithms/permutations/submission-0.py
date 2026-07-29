class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        used=[False]*n

        def solve(sub):
            if len(sub)==len(nums):
                res.append(sub[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i]=True
                sub.append(nums[i])
                solve(sub)
                sub.pop()
                used[i]=False

            
            
        
        solve([])
        return res
                

        