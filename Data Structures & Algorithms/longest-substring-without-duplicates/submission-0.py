class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        for i in range(len(s)):
            my_set=set()
            count=0
            while i<len(s) and s[i] not in my_set:
                count+=1
                my_set.add(s[i])
                maxi=max(maxi,count)
                i+=1
        return maxi



        