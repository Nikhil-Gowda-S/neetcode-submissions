class Solution:
    def isPalindrome(self, s: str) -> bool:
        char=[]
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                char.append(i)
        print(char)
        return char==char[::- 1]
        