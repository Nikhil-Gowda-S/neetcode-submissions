class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isdigit() or (i.startswith("-") and len(i)>1):
                stack.append(i)
            elif i in "+-/*":
                ele1=int(stack.pop())
                ele2=int(stack.pop())
                if i=="+":
                    stack.append(ele2+ele1)
                if i=="-":
                    stack.append(ele2-ele1)
                if i=="*":
                    stack.append(ele2*ele1)
                if i=="/":
                    
                    stack.append(ele2/ele1)
        return int(stack[0])
                