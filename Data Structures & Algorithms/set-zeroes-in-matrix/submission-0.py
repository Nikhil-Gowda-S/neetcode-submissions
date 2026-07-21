class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        row_mark=[0]*r
        col_mark=[0]*c 
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row_mark[i]=1
                    col_mark[j]=1
        for i in range(r):
            for j in range(c):
                if row_mark[i]==1 or col_mark[j]==1:
                    matrix[i][j]=0
