class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1=0
            rob2=0
            for n in nums:
                maxrob=max(n+rob1,rob2)
                rob1=rob2
                rob2=maxrob
            return rob2
        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
