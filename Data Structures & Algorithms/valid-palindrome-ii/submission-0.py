class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def checkpalindrome(string):
            left=0
            right=len(string)-1
            while left<=right:
                if string[left]!=string[right]:
                    return False
                left+=1
                right-=1
            return True
        while l<r:
            if s[l]!=s[r]:
                return checkpalindrome(s[l+1:r+1]) or checkpalindrome(s[l:r])
            l+=1
            r-=1
        return True
        