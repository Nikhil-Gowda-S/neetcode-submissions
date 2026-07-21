class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        def solve(i):
            if i==0:
                return nums[i]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick=nums[i]+solve(i-2)
            not_pick=solve(i-1)
            dp[i]=max(pick,not_pick)  
            return dp[i]     
        return solve(len(nums)-1)