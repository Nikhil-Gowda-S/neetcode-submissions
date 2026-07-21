class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        leng=len(nums)
        low=0
        high=leng-1
        if leng%2==1:
            return nums[(low+high)//2]
        else:
            return (nums[(low+high)//2]+nums[((low+high)//2)+1])/2
        