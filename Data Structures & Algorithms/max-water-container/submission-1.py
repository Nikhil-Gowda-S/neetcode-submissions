class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxi=0
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                width=j-i
                height=min(nums[i],nums[j])
                content=width*height
                maxi=max(maxi,content)
        return maxi

"""class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            width = right - left
            curr = width * min(height[left], height[right])
            ans = max(ans, curr)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans"""
        