class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def solve(idx,total,sub):
            if idx>=len(nums):
                if total==target:
                    temp=sub[:]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                return
            if total>target:
                return
            sub.append(nums[idx])
            solve(idx,total+nums[idx],sub)
            sub.pop()
            solve(idx+1,total,sub)
        solve(0,0,[])
        return res
        