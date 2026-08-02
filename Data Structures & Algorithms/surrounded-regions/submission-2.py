class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row=len(board)
        col=len(board[0])
        vis=[[-1 for _ in range(col)] for _ in range(row)]
        def dfs(i,j,r,c,board,vis):
            if vis[i][j]!=-1:
                return
            if board[i][j]=="X":
                return
            vis[i][j]=1
            for di,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x,new_y=di+i,dy+j
                if new_x<0 or new_x>=r or new_y<0 or new_y>=c:
                    continue
                if vis[new_x][new_y]!=-1:
                    continue
                if board[new_x][new_y]=="X":
                    continue
                dfs(new_x,new_y,r,c,board,vis)
        for i in range(col):
            if vis[0][i]==-1:
                dfs(0,i,row,col,board,vis)
            if vis[row-1][i]==-1:
                dfs(row-1,i,row,col,board,vis)
        for i in range(row):
            if vis[i][0]==-1:
                dfs(i,0,row,col,board,vis)
            if vis[i][col-1]==-1:
                dfs(i,col-1,row,col,board,vis)
        for i in range(row):
            for j in range(col):
                if board[i][j]=="X" or vis[i][j]==-1:
                    board[i][j]="X"
        

        