class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        
        for i in range(r):
            if target<=matrix[i][-1]:
                low=0
                high=c-1
                while low<=high:
                    mid=(low+high)//2
                    if matrix[i][mid]==target:
                        return True
                    if matrix[i][mid]>target:
                        high=mid-1
                    else:
                        low=mid+1
        return False
        