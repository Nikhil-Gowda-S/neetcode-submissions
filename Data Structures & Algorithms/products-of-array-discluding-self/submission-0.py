class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            e=nums.pop(i)
            mul=1
            for j in nums:
                mul*=j
            res.append(mul)
            nums.insert(i,e)
        return res

    

        