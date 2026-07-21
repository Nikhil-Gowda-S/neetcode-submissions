class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxi=-10001
        for i in range(len(nums)):
            cur=0
            for j in range(i,len(nums)):
                cur+=nums[j]
                maxi=max(maxi,cur)
        return maxi

        