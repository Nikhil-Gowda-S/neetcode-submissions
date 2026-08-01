class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,r,c,grid,vis):
            if vis[i][j]!=-1:
                return
            if grid[i][j]=="0":
                return
            vis[i][j]=1
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x,new_j=i+dx,j+dy
                if new_x<0 or new_x>=r or new_j<0 or new_j>=c:
                    continue
                if vis[new_x][new_j]==1:
                    continue
                if grid[new_x][new_j]=="0":
                    continue
                dfs(new_x,new_j,r,c,grid,vis)
        row=len(grid)
        col=len(grid[0])
        vis=[[-1 for _ in range(col)] for _ in range(row)]
        count=0
        for i in range(row):
            for j in range(col):

                if vis[i][j]==-1 and grid[i][j]!="0":
                    dfs(i,j,row,col,grid,vis)
                    count+=1
        return count

        