class Solution:
    def isValid(self, s: str) -> bool:
        dic={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if dic[i]==stack[-1]:
                    stack.pop()
                elif dic[i]!=stack[-1]:
                    return False 
        if len(stack)==0:
            return True
        else:
            return False
        