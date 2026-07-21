class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        sub=[]
        def solve(i,sub):
            if i==len(nums):
                temp=sub[:]
                temp.sort()
                if temp not in res:
                    res.append(temp)
                return 
            sub.append(nums[i])
            solve(i+1,sub) 
            sub.pop()
            solve(i+1,sub)
        solve(0,[])
        return res  
        