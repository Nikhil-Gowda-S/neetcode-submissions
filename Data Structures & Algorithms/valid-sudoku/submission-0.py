class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # check row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # check column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # check box
                box = (r // 3) * 3 + (c // 3)
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        
        return True