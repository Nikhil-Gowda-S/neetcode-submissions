class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        k=0
        for i in nums:
            if i not in s:
                s.add(i)
                nums[k]=i
                k+=1
                
        return k

        