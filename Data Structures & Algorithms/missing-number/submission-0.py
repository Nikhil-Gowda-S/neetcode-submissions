class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res1=n
        res2=0
        for i in range(n):
            res1^=i
            res2^=nums[i]
        return res1^res2
        
        
        