class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res=set()
        for i in nums: 
            if i in res:
                return i
            else:
                res.add(i)
        