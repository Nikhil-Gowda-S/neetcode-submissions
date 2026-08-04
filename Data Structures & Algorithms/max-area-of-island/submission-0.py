class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def dfs(i,j,r,c,grid,vis):
            if vis[i][j]!=-1:
                return 0
            if grid[i][j]==0:
                return 0
            vis[i][j]=1
            count=1
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x,new_j=i+dx,j+dy
                if new_x<0 or new_x>=r or new_j<0 or new_j>=c:
                    continue
                if vis[new_x][new_j]==1:
                    continue
                if grid[new_x][new_j]==0:
                    continue
                count+=dfs(new_x,new_j,r,c,grid,vis)
            return count
        maxi=0
                
        vis=[[-1 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if vis[i][j]==-1 and grid[i][j]==1:
                    count=dfs(i,j,row,col,grid,vis)
                    maxi=max(maxi,count)
        return maxi






        