class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=len(s)
        left=0
        freq={}
        maxi=0
        ans=0
        for right in range(l):
            freq[s[right]]=freq.get(s[right],0)+1
            maxi=max(maxi,freq[s[right]])
            while (right-left+1)-maxi>k:
                freq[s[left]]-=1
                left+=1
            ans=max(right-left+1,maxi)
        return ans
        


        