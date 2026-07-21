class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        sorted_list = list(sorted(d.items(), key=lambda x: x[1]))
        res=[]
        while k>0:
            res.append(sorted_list.pop()[0])
            k-=1
        return res
