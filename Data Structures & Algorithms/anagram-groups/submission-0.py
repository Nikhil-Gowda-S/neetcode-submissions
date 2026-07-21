class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        
        for i in range(len(strs)):
            ans=[]
            if "".join(sorted(strs[i])) not in res:
                res["".join(sorted(strs[i]))]=[i]
            else:
                res["".join(sorted(strs[i]))].append(i)
        ans=[]
        for indices in res.values():
            group = [strs[i] for i in indices]
            ans.append(group)

        return ans
        

        


        
            
        