class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def solve(i,l,sub):
            if i>=len(nums):
                res.append(sub[:])
                return 
            sub.append(nums[i])
            solve(i+1,l+1,sub) 
            sub.pop()
            solve(i+1,l,sub)
        solve(0,0,[])
        return res           
        