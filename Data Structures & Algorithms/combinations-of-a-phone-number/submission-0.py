class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        if digits=="":
            return []
        def solve(idx,sub):
            if idx>=len(digits):
                res.append("".join(sub))
                return
            for ch in maps[digits[idx]]:
                sub.append(ch)
                solve(idx+1,sub)
                sub.pop()
        solve(0,[])
        return res



        