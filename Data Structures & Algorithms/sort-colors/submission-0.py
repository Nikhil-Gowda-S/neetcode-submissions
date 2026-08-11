class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0=0
        count_1=0
        count_2=0
        for i in nums:
            if i==0:
                count_0+=1
            if i==1:
                count_1+=1
            if i==2:
                count_2+=1
        for i in range(count_0):
            nums[i]=0
        for i in range(count_0,count_0+count_1):
            nums[i]=1
        for i in range(count_0+count_1,count_0+count_1+count_2):
            nums[i]=2
        