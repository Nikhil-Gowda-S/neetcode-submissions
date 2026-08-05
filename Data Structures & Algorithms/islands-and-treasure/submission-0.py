class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        vis=[[-1 for _ in range(cols)]for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append([i,j])
                    vis[i][j]=1
        def addrows(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==-1 or vis[r][c]==1): 
                return 
            
            
            vis[r][c]=1
            queue.append([r,c])

        dist=0
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                grid[r][c]=dist
                for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                    new_x,new_y=r+dx,c+dy
                    addrows(new_x,new_y)
            dist+=1
                

                
        
        