from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
            res=[]
            for i in range(4):
                j=str((int(lock[i])+1)%10)
                digit=lock[:i]+j+lock[i+1:]
                res.append(digit)
                j=str((int(lock[i])-1+10)%10)
                digit=lock[:i]+j+lock[i+1:]
                res.append(digit)
            return res
            
        queue=deque()
        queue.append(["0000",0])
        vis=set(deadends)
        while queue:
            l,count=queue.popleft()
            if l==target:
                return count
            for lock in children(l):
                if lock not in vis:
                    vis.add(lock)
                    queue.append([lock,count+1])
        return -1
            
        
        