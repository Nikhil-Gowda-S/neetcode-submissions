class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n != 0:
            if n&1==1:
                count+=1
                
            n=n>>1
        return count
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            res.append(self.hammingWeight(i))
        return res
            
        