from collections import deque
from copy import deepcopy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis=deepcopy(grid)
        fresh_count=0
        row=len(grid)
        col=len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh_count+=1
        queue=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append([i,j])
        minutes=0
        while len(queue)!=0 and fresh_count>0:
            minutes+=1
            total_rotten=len(queue)
            for _ in range(total_rotten):
                r,c=queue.popleft()
                for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                    new_r,new_c=r+i,c+j
                    if new_r<0 or new_r>=row or new_c<0 or new_c>=col:
                        continue
                    if vis[new_r][new_c]==2 or vis[new_r][new_c]==0:
                        continue
                    fresh_count-=1
                    vis[new_r][new_c]=2
                    queue.append([new_r,new_c])
        if fresh_count>0:
            return -1
        return minutes

                
                
                

            
            
        



        
        